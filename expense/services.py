from django.db import connections
from django.conf import settings
from django.utils import timezone
import datetime
from django.db.models import Count, Max, Sum
from dateutil.relativedelta import relativedelta
from dateutil import parser

from django.template import Context
from django.template.loader import get_template

from .models import ExpenseItem, ExpenseCategory
from .mailer import MailerManager

def get_current_month():
    current_datetime = timezone.now()
    return datetime.datetime(current_datetime.year, current_datetime.month, 1)

def hash_list_reverse(hash_list):
    return list(reversed(hash_list))


""" CURRENT EXPENSE """

def get_recent_expenses():
    current_datetime = timezone.now()
    current_month = datetime.datetime(current_datetime.year, current_datetime.month, 1)

    queryset = ExpenseItem.objects.filter(created_at__gt = current_month).order_by('-created_at')
    aggregated_data = queryset.aggregate(total_cost=Sum('cost'), transactions=Count('id'))

    return { 'objects': queryset, 'info': aggregated_data }


""" HISTORY """

def get_month_history():
    queryset = ExpenseItem.objects.filter(created_at__lt = get_current_month()).extra(select={'month': connections[ExpenseItem.objects.db].ops.date_trunc_sql('month', 'created_at')}).values('month').annotate(count=Count('created_at'), total_cost=Sum('cost'))

    return list(reversed(queryset))

def get_month_detailed_history(month=None):
    month = parser.parse(month)
    month_begin = month + relativedelta(month=month.month)
    month_end = month_begin + relativedelta(month=month.month+1)

    queryset = ExpenseItem.objects.filter(created_at__gt=month_begin).filter(created_at__lt=month_end).order_by('created_at')
    aggregated_data = queryset.aggregate(total_cost=Sum('cost'), transactions=Count('id'))

    if queryset:
        return { 'objects': queryset, 'info': aggregated_data }

    return False


""" REPORTS """

def prepare_report_data(month_date):
    month = parser.parse(month_date)
    #month_date = month
    month_begin = month + relativedelta(month=month.month-1)
    month_end = month_begin + relativedelta(month=month.month)

    queryset = ExpenseItem.objects.filter(created_at__gt=month_begin).filter(created_at__lt=month_end)


    """ Group expenses by category """
    grouped_by_category = {}
    for item in queryset.all():
        try:
            date_key = item.category.name
        except:
            date_key = 'Uncategorized'

        if date_key in grouped_by_category:
            grouped_by_category[date_key].append(item)
        else:
            grouped_by_category[date_key] = [item]

    """ Group expenses by day """
    grouped_by_date = {}
    for item in queryset.all():
        date_key = item.created_at.strftime('%Y-%m-%d')
        if date_key in grouped_by_date:
            grouped_by_date[date_key].append(item)
        else:
            grouped_by_date[date_key] = [item]

    """ Expenses by date summary """
    summary_by_date = queryset.extra({'weekday': "date(created_at)"}).values('weekday').annotate(Count('id'), total_cost=Sum('cost'))

    for summary in summary_by_date:
        if summary['weekday'] in grouped_by_date:
            summary['objects'] = []
            for expense in grouped_by_date[summary['weekday']]:
                summary['objects'].append(expense)

    """ All expenses """
    all_expenses = queryset.all()

    """ Total summary """
    summary_total = queryset.order_by('created_at').aggregate(total_cost=Sum('cost'), transactions=Count('id'))
    summary_total['date'] = month_begin.strftime('%Y-%m')

    return { 'all_expenses': all_expenses, 'grouped_by_category': grouped_by_category, 'grouped_by_date': grouped_by_date, 'summary_by_date': summary_by_date, 'summary_total': summary_total }


def send_report(month_date):
    """ This is typically used by cron/at so every 'print' goes straight to the log files """
    report_date = str(month_date.year)+'-'+str(month_date.month)+'-01'
    report_data = prepare_report_data(report_date)

    template = get_template('mailer/expense_report.html')
    try:
        html = template.render(Context({'expenses': report_data}))
    except Exception as e:
        print "Unexpected error while rendering template:", e

    mailer = MailerManager()
    mailer.set_body(html)
    mailer.send()


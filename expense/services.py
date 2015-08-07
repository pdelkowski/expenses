from django.db import connections
from django.utils import timezone
from django.db.models import Count, Max, Sum
import datetime
from dateutil.relativedelta import relativedelta
from dateutil import parser

from .models import ExpenseItem, ExpenseCategory

def get_current_month():
    current_datetime = timezone.now()
    return datetime.datetime(current_datetime.year, current_datetime.month, 1)

def get_recent_expenses():
    current_datetime = timezone.now()
    current_month = datetime.datetime(current_datetime.year, current_datetime.month, 1)
    queryset = ExpenseItem.objects.filter(created_at__gt = current_month).order_by('-created_at')
    return queryset

def get_month_history():
    queryset = ExpenseItem.objects.filter(created_at__lt = get_current_month()).extra(select={'month': connections[ExpenseItem.objects.db].ops.date_trunc_sql('month', 'created_at')}).values('month').annotate(count=Count('created_at'), total_cost=Sum('cost'))

    return list(reversed(queryset))

def get_month_detailed_history(month=None):
    month = parser.parse(month)
    month_begin = month + relativedelta(month=month.month)
    month_end = month_begin + relativedelta(month=month.month+1)

    #queryset = ExpenseCategory.objects.filter(item__created_at__range=[month_begin, month_end])#.annotate(Sum("item__cost")).order_by('-created_at')
    queryset = ExpenseItem.objects.filter(created_at__gt=month_begin).filter(created_at__lt=month_end).order_by('created_at')
    aggregated_data = queryset.aggregate(total_cost=Sum('cost'), transactions=Count('id'))

    if queryset:
        return { 'objects': queryset, 'info': aggregated_data }

    return False




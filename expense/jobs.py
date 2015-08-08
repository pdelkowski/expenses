from django_cron import CronJobBase, Schedule
from django.conf import settings
from django.utils import timezone

from .services import prepare_report_data, get_current_month, send_report

class ExpenseReportJob(CronJobBase):
    RUN_EVERY_MINS = 1440 # 1 day

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'expense.expense_report'

    def do(self):
        print '--------------------------------'

        current_date = timezone.now()
        if int(current_date.day) == settings.REPORT_DAY_OF_MONTH:
            print '---------- SEDNING -----------'
            month_date = get_current_month()
            send_report(month_date)
        else:
            print '---------- NO REPORTS TO SEND -----------'



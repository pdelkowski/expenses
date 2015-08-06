from .models import ExpenseItem
from django.utils import timezone
import datetime

def get_recent_expenses():
    current_datetime = timezone.now()
    current_month = datetime.datetime(current_datetime.year, current_datetime.month, 1)
    queryset = ExpenseItem.objects.filter(created_at__gt = current_month).order_by('-created_at')
    return queryset

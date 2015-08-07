from django.db import models
from django.utils import timezone

def created_at_current_time():
    return timezone.now()

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField('date published')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class ExpenseItem(models.Model):
    category = models.ForeignKey(ExpenseCategory, blank=True, null=True, related_name='items', related_query_name='item')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='No description')
    cost = models.FloatField(default=0)
    created_at = models.DateTimeField(default=created_at_current_time())

    def __unicode__(self):
        return self.name

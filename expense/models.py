from django.db import models

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField('date published')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class ExpenseItem(models.Model):
    category = models.ForeignKey(ExpenseCategory, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='No description')
    cost = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return self.name

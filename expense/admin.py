from django.contrib import admin
from django.contrib.auth.models import User, Group
from expense.models import ExpenseItem, ExpenseCategory

# Unregister default user and group models
admin.site.unregister(User)
admin.site.unregister(Group)

# Register expense items and categories
admin.site.register(ExpenseItem)
admin.site.register(ExpenseCategory)

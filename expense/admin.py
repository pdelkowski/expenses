from django.contrib import admin
from django.contrib.auth.models import User, Group
from expense.models import ExpenseItem, ExpenseCategory

# Unregister default user and group models
admin.site.unregister(User)
admin.site.unregister(Group)

# Register expense items and categories
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'cost', 'category')
    list_filter = ('created_at', 'category')
    search_fields = ('name',)

admin.site.register(ExpenseItem, ItemAdmin)
admin.site.register(ExpenseCategory)

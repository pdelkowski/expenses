from django import forms

from .models import ExpenseItem

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = ExpenseItem
        fields = ['name', 'description', 'category']

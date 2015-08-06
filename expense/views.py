from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import FormView, CreateView
from django.utils import timezone

from .models import ExpenseItem, ExpenseCategory
from .services import *
from .forms import ExpenseForm

class CurrentView(generic.ListView):
    template_name = 'current/index.html'
    context_object_name = 'latest_expense_list'

    def get_queryset(self):
        return get_recent_expenses()

class ExpenseNewView(FormView):
    template_name = 'expense/new.html'
    form_class = ExpenseForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ExpenseNewView, self).get_context_data(**kwargs)
        context['categories'] = ExpenseCategory.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super(ExpenseNewView, self).form_valid(form)

from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import FormView, CreateView
from django.utils import timezone

from .models import ExpenseItem, ExpenseCategory
from .services import *
from .forms import ExpenseForm

class CurrentView(generic.ListView):
    template_name = 'current/index.html'
    context_object_name = 'latest_expenses'

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

class HistoryListView(generic.ListView):
    template_name = 'history/index.html'
    context_object_name = 'expenses_monthly'

    def get_queryset(self):
        return get_month_history()

class HistoryDetailView(generic.ListView):
    template_name = 'history/detail.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        month = self.kwargs['param_date']+'-01' # eg. param_date = 2015-05, so we have 2015-05-01 we start from first day of the month
        result = get_month_detailed_history(month)

        if result == False:
            raise Http404("Couldn't fetch any data with provided date")

        return result

def test(request):
    month_date = get_current_month()
    report_date = str(month_date.year)+'-'+str(month_date.month)+'-01'
    r = prepare_report_data(report_date)
    #return render_to_response('mailer/expense_report.html', {'expenses': r}, context_instance=RequestContext(request))
    return HttpResponse('testing...')

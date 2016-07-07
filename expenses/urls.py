from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from expense import views

urlpatterns = [
    url(r'^$', views.CurrentView.as_view(), name='current'),
    url(r'^expense/new$', views.ExpenseNewView.as_view(), name='expense_new'),
    url(r'^history$', views.HistoryListView.as_view(), name='history'),
    url(r'^history/details/(?P<param_date>[0-9]{4}-[0-9]{2})$',
        views.HistoryDetailView.as_view(), name='history_detail'),
    url(r'^test$', views.test, name='test'),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

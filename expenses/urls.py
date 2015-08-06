from django.conf.urls import include, url
from django.contrib import admin

from expense import views

urlpatterns = [
    url(r'^$', views.CurrentView.as_view(), name='current'),
    url(r'^expense/new$', views.ExpenseNewView.as_view(), name='expense_new'),
    url(r'^admin/', include(admin.site.urls)),
]

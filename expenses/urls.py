from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^expenses$', views.expenses_list),
    url(r'^expenses/(?P<pk>[0-9]+)$', views.expenses_detail)
]

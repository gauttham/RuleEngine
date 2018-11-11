from . import views

from django.conf.urls import url

urlpatterns = [
    url(r'v1/signal/$', views.SignalDataView.as_view()),
    url(r'v1/rule/$', views.RuleListView.as_view()),
    url(r'v1/load/$', views.triggerLoader.as_view()),
]
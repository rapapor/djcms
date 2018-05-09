#from django.urls import path
from django.conf.urls import include, url
from views import JobsListView, JobsDetailView

from . import views

urlpatterns = [    
    url(r'^$', JobsListView.as_view(), name='job_joboffer_list'),
    url(r'^(?P<slug>[-\w]+)/$', JobsDetailView.as_view(), name='job_joboffer_detail'),
]
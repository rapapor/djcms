#from django.urls import path
from django.conf.urls import include, url
from views import DistributorList

from . import views

urlpatterns = [    
    url(r'^$', DistributorList.as_view(), name='distributor_list'),    
]
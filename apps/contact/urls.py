#from django.urls import path
from django.conf.urls import include, url
from views import ContactList

from . import views

urlpatterns = [    
    url(r'^$', ContactList.as_view(), name='contact_list'),    
]
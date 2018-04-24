#from django.urls import path
from django.conf.urls import include, url
from views import ProductListView, ProductDetailView

from . import views

urlpatterns = [    
    url(r'^$', ProductListView.as_view(), name='product_list'),
    url(r'^(?P<slug>[-\w]+)/$', ProductDetailView.as_view(), name='product_detail'),
]
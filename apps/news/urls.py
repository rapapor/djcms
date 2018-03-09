#from django.urls import path
from django.conf.urls import include, url
from views import NewsListView, NewsDetailView

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #url(r'', views.index, name='index')
    url(r'^$', NewsListView.as_view(), name='news_list'),
    url(r'^(?P<slug>[-\w]+)/$', NewsDetailView.as_view(), name='news_detail'),
]
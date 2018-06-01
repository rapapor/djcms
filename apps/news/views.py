import datetime
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.shortcuts import render
from models import News

# Create your views here.
from django.http import HttpResponse


class NewsListView(ListView):
    # model = News
    queryset=News.objects.filter(pub_date__lte=datetime.datetime.now()).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)            
        context['now'] = timezone.now()
        return context


class NewsDetailView(DetailView):

    model = News

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
     
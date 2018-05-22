# -*- coding: utf-8 -*-
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.shortcuts import render
from models import Distributor

# Create your views here.
from django.http import HttpResponse


class DistributorList(ListView):
    queryset=Distributor.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super(DistributorList, self).get_context_data(**kwargs)
        context['distributors'] = self.queryset.filter(active=True)
        context['distributor'] = self.queryset.filter(active=True).count()
        return context

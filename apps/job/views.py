# -*- coding: utf-8 -*-
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.shortcuts import render
from models import JobOffer

# Create your views here.
from django.http import HttpResponse


class JobsListView(ListView):
    queryset=JobOffer.objects.all()
    # model = JobOffer.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super(JobsListView, self).get_context_data(**kwargs)
        context['active_job_offer'] = self.queryset.filter(active=True)
        context['active_job_offer_count'] = self.queryset.filter(active=True).count()
        return context


class JobsDetailView(DetailView):
    
    model = JobOffer

    def get_context_data(self, **kwargs):
        context = super(JobsDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()          
        return context
# -*- coding: utf-8 -*-
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.shortcuts import render
from models import Contact

# Create your views here.
from django.http import HttpResponse


class ContactList(ListView):
    queryset=Contact.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super(ContactList, self).get_context_data(**kwargs)
        context['contacts'] = self.queryset.filter(active=True)
        context['contact'] = self.queryset.filter(active=True).count()
        return context

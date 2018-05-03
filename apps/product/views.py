from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.shortcuts import render
from models import Product, LogisticData

# Create your views here.
from django.http import HttpResponse


class ProductListView(ListView):
	model = Product

	def get_context_data(self, **kwargs):
        	context = super(ProductListView, self).get_context_data(**kwargs)
        	context['now'] = timezone.now()
        	return context


class ProductDetailView(DetailView):

    model = Product

    def get_context_data(self, **kwargs):
        	context = super(ProductDetailView, self).get_context_data(**kwargs)
        	context['now'] = timezone.now()
        	return context
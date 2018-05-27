# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from cms.models.fields import PlaceholderField
from ..product.models import Product


class Distributor(models.Model):
	active = models.BooleanField(
		default=True,
		verbose_name="Aktywny Tak/Nie",
		help_text=u"Zaznacz jezeli chcesz wyswietlic dystrybutora"
	)

	biz_name_pl = models.CharField(
		max_length=200, 
		verbose_name='Nazwa firmy PL'
	)

	biz_name_en = models.CharField(
		max_length=200, 
		verbose_name='Nazwa firmy EN'
	)

	woj_pl = models.CharField(
		max_length=200, 
		verbose_name='wojewodztwo PL'
	)

	woj_en = models.CharField(
		max_length=200, 
		verbose_name='wojewodztwo EN'
	)

	street_pl = models.CharField(
		max_length=200, 
		verbose_name='ulica i kod pocztowy PL'
	)

	street_en = models.CharField(
		max_length=200, 
		verbose_name='ulica i kod pocztowy EN'
	)

	phone = models.CharField(
		max_length=200, 
		verbose_name='telefon'
	)

	gmapCoordynator_x = models.CharField(
		max_length=200, 
		verbose_name='koordynaty google map x'
	)

	gmapCoordynator_y = models.CharField(
		max_length=200, 
		verbose_name='koordynaty google map y'
	)

	distributor_file = models.ImageField(
		upload_to='media/media/dist/',
		blank=True,
		null=True,
		verbose_name="Miniaturka"
	)

	products = models.ManyToManyField(Product)

  	def __unicode__(self):
  		return self.biz_name_pl

  	def __str__(self):
  		return self.biz_name_en
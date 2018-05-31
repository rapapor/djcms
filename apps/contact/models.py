# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from cms.models.fields import PlaceholderField



class Contact(models.Model):

	SECTION_CHOICES = (
        ('SELLER', 'seller'),
        ('BUYER', 'buyer'),
        ('PRODUCTION', 'production'),
        ('HR', 'hr'),
    )


	active = models.BooleanField(
		default=True,
		verbose_name="Aktywny Tak/Nie",
		help_text=u"Zaznacz jezeli chcesz wyswietlic kontakt"
	)

	name_pl = models.CharField(
		max_length=200, 
		verbose_name='Imie Nazwisko PL'
	)

	name_en = models.CharField(
		max_length=200, 
		verbose_name='Imie Nazwisko EN'
	)

	position_pl = models.CharField(
		max_length=200, 
		verbose_name='Stanowisko PL'
	)

	position_en = models.CharField(
		max_length=200, 
		verbose_name='Stanowisko EN'
	)

	email = models.CharField(
		max_length=200, 
		verbose_name='email'
	)

	phone = models.CharField(
		max_length=200, 
		verbose_name='telefon'
	)

	section = models.CharField(max_length=20, choices=SECTION_CHOICES, default='SELLER')
	

	contact_file = models.ImageField(
		upload_to='media/media/contact/',
		blank=True,
		null=True,
		verbose_name="Miniaturka"
	)

  	def __unicode__(self):
  		return self.name_pl

  	def __str__(self):
  		return self.name_en
# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from cms.models.fields import PlaceholderField
# Create your models here.


class News(models.Model):
	title_pl = models.CharField(max_length=200, verbose_name='Tytul PL')
	title_en = models.CharField(max_length=200, verbose_name='Tytul EN')
	pub_date = models.DateField(default=timezone.now, verbose_name='data publikacji')
	#content_pl = models.TextField(verbose_name='Tresc PL') 
	#content_en = models.TextField(verbose_name='Tresc EN')
	tip_pl = models.CharField(max_length=200, verbose_name='tekst zachety PL')
	tip_en = models.CharField(max_length=200, verbose_name='tekst zachety EN')

	image = models.ImageField(
		verbose_name='zdjecie na liste newsow',
		upload_to='media/aktualnosci/',
		blank=True,
		null=True,		
		)

	image_start = models.ImageField(
		verbose_name='zdjecie na pierwsza strone',
		upload_to='media/aktualnosci/',
		blank=True,
		null=True,
		help_text=u"sugerowana wielkosc 760x612"
		)

	image_big = models.ImageField(
		verbose_name='zdjecie duze do tresci',
		upload_to='media/aktualnosci/',
		blank=True,
		null=True,
		help_text=u"sugerowana wielkosc 870x412"
		)

	slug = models.SlugField(max_length=50, default='')

	content_pl = PlaceholderField(slotname="content_pl", related_name="news_content_pl")
	content_en = PlaceholderField(slotname="content_en", related_name="news_content_en")


	def get_absolute_url(self):
		return reverse('news:news_detail', kwargs={'slug': self.slug, })

	def getlistArticle(self):		
		return News.objects.filter(pub_date__lte=datetime.datetime.now()).order_by('-pub_date')[:5]

	@classmethod		
	def getLastNews(cls):
		return News.objects.latest("pub_date")
	
  	def __unicode__(self):
  		return self.title_pl

  	def __str__(self):
  		return self.title_en
	




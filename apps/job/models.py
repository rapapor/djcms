from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from cms.models.fields import PlaceholderField

# Create your models here.
class JobOffer(models.Model):

	active = models.BooleanField(
		default=False,
		verbose_name="Aktywne Tak/Nie",
		help_text=u"Zaznacz jezeli chcesz opublikowac ogloszenie"
	)

	pub_date = models.DateField(
		default=timezone.now, 
		verbose_name='data publikacji'
	)

	position_pl = models.CharField(
		max_length=200, 
		verbose_name='stanowisko PL'
	)

	position_en = models.CharField(
		max_length=200, 
		verbose_name='stanowisko EN'
	)

	city = models.CharField(
		max_length=200, 
		verbose_name='Miasto'
	)

	content_pl = PlaceholderField(
		slotname="content_pl", 
		related_name="job_offer_PL"
	)
	content_en = PlaceholderField(
		slotname="content_en", 
		related_name="job_offer_EN"
	)


	time_size = models.CharField(
		max_length=200, 
		verbose_name='Wielkosc etatu'
	)


	slug = models.SlugField(
		max_length=50, 
		default=''
	)

  	def __str__(self):
  		return self.position_pl

	def getlistoffer(self):		
		return JobOffer.objects.filter(active = True)

 
	def get_absolute_url(self):
		return reverse('job:joboffer_detail', kwargs={'slug': self.slug, })


 	
 		 
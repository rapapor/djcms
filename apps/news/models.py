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
	image = models.ImageField(upload_to='media/', blank=True, null=True)
	slug = models.SlugField(max_length=50, default='')

	content_pl = PlaceholderField(slotname="content_pl", related_name="news_content_pl")
	content_en = PlaceholderField(slotname="content_en", related_name="news_content_en")


	def get_absolute_url(self):
		return reverse('news:news_detail', kwargs={'slug': self.slug, })

	def getlistArticle(self):		
		return News.objects.all()[:5]



	




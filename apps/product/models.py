# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from cms.models.fields import PlaceholderField
from django.utils import timezone
from django.utils.safestring import mark_safe


# Create your models here.
class Product(models.Model):

	CATEGORY = (
        ('gastro', 'Gastronomia'),
        ('biz', 'Biznes'),
        
    )


	best_seller = models.BooleanField(
		default=False,
		verbose_name="Bestseller Tak/Nie",
		help_text=u"Zaznacz jeżeli produkt ma być bestsellerem"
	)

	best_seller_file = models.ImageField(
		upload_to='media/media/bestSellerMini/',
		blank=True,
		null=True,
		verbose_name="Miniaturka Bestsellera 322x307px"
	)

	product_mini_file = models.ImageField(
		upload_to='media/media/produkt_mini/',
		blank=True,
		null=True,
		verbose_name="Miniaturka 370x278px"
	)

	name_pl = models.CharField(
		max_length=50,
		verbose_name='Nazwa PL'
	)

	name_en = models.CharField(
		max_length=50,
		verbose_name='Nazwa EN'
	)

	desc_mini_pl = models.CharField(
		max_length=150,
		verbose_name='Zajawka PL'
	)

	desc_mini_en = models.CharField(
		max_length=150, 
		verbose_name='Zajawka EN'
	)

	category = models.CharField(
		max_length=25,
		choices=CATEGORY,
		default='gastro'
	)

	desc_pl = models.TextField(
		verbose_name='Opis PL'
	)

	desc_en = models.TextField(
		verbose_name='Opis EN'
	)

	product_file_1 = models.ImageField(
		upload_to='media/media/produkt_img/',
		blank=True,
		null=True,
		verbose_name="Produkt zdjecie 1 "
	)

	product_file_2 = models.ImageField(
		upload_to='media/media/produkt_img/', 
		blank=True, 
		null=True,
		verbose_name="Produkt zdjecie 2 "
	)

	product_file_3 = models.ImageField(
		upload_to='media/media/produkt_img/', 
		blank=True, 
		null=True,
		verbose_name="Produkt zdjecie 3 "
	)
	

	slug = models.SlugField(
		max_length=50, 
		default=''
	)

	content_pl = PlaceholderField(
		slotname="content_pl",
		related_name="product_content_pl"
	)
	content_en = PlaceholderField(
		slotname="content_en", 
		related_name="product_content_en"
	)

	spprzyg_pl = PlaceholderField(
		slotname="sposob przygotowania pl", 
		related_name="createed_example_pl"
	)

	spprzyg_en = PlaceholderField(
		slotname="sposob przygotowania en", 
		related_name="createed_example_en"
	)

	def getLogisticData(self):
		return LogisticData.objects.filter(Logistic_data = self)
	
	def get_absolute_url(self):
		return reverse('product:product_detail', kwargs={'slug': self.slug, })

	def getlistProduct(self):		
		return Product.objects.all()

	@classmethod
	def getBestSeller(cls):
		return Product.objects.filter(best_seller=True)[:4]

	@classmethod	
	def getRandomProduct(cls):
		return Product.objects.all().order_by('?')[:2]

	def thumbnail(self):
  		return mark_safe(
  			'<img width="40" height="40" src="/media/{}" />'.format(
  				self.product_mini_file))

  	def __unicode__(self):
  		return self.name_pl

  	def __str__(self):
  		return self.name_en

class LogisticData(models.Model):
 	"""docstring for LogisticData"""
 	Logistic_data = models.ForeignKey(
 		'Product', 
 		on_delete=models.SET_NULL,
 		null=True,
		blank=False,
		default='',
		help_text=u'Wybierz dane logistyczne dla produktu',
		max_length=60
	)


 	product_name_pl = models.CharField(
 		blank=True, 
 		null=True, 
 		max_length=50, 
 		verbose_name='Nazwa PL'
 	)

 	product_name_en =  models.CharField(
 		blank=True, 
 		null=True, 
 		max_length=50, 
 		verbose_name='Nazwa EN'
 	)

 	form_pl = models.CharField(
 		blank=True, 
 		null=True, 
 		max_length=50, 
 		verbose_name='Forma PL'
 	)

 	form_en =  models.CharField(
 		blank=True, 
 		null=True, 
 		max_length=50, 
 		verbose_name='Forma EN'
 	)

 	single_pack_pl = models.CharField(
 		blank=True, 
 		null=True, 
 		max_length=50,
 		verbose_name='Opakowanie jedn. PL'
 	)

 	single_pack_en =  models.CharField(
 		blank=True, 
 		null=True, 
 		max_length=50,
 		verbose_name='Opakowanie jedn. EN'
 	) 	

 	multi_pack_pl = models.CharField(
 		blank=True, 
 		null=True, 
 		max_length=50,
 		verbose_name='Paletyzacja PL'
 	)

 	multi_pack_en = models.CharField(
 		blank=True, 
 		null=True, 
 		max_length=50,
 		verbose_name='Paletyzacja EN'
 	)

 
	


 	
 		 
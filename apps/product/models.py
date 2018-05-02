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

	pizza_pl = models.TextField(
		blank=True, 
		null=True,
		verbose_name='Piec do pizzy PL'
	)

	pizza_en = models.TextField(
		blank=True, 
		null=True,
		verbose_name='Piec do pizzy EN'
	)

	bake_kon_pl = models.TextField(
		blank=True, 
		null=True,
		verbose_name='Piec konwekcyjny PL'

	)

	bake_kon_en = models.TextField(
		blank=True, 
		null=True,
		verbose_name='Piec konwekcyjny EN'
	)

	mikrofave_pl = models.TextField(
		blank=True, 
		null=True,
		verbose_name='Mikrofala PL'
	)

	mikrofave_en = models.TextField(
		blank=True, 
		null=True,
		verbose_name='Mikrofala EN'
	)

	pan_pl = models.TextField(
		blank=True, 
		null=True,
		verbose_name='Patelnia PL'
	)

	pan_en = models.TextField(
		blank=True, 
		null=True,
		verbose_name='Patelnia EN'
	)

	pot_pl = models.TextField(
		blank=True, 
		null=True,
		verbose_name='Garnek PL'
	)

	pot_en = models.TextField(
		blank=True, 
		null=True,
		verbose_name='Garnek EN'
	)

	bake_pl = models.TextField(
		blank=True, 
		null=True,
		verbose_name='Piekarnik PL'
	)

	bake_en = models.TextField(
		blank=True, 
		null=True,
		verbose_name='Piekarnik EN'
	)

	toaster_op_pl = models.TextField(
		blank=True, 
		null=True,
		verbose_name='Opiekacz PL'
	)

	toaster_op_en = models.TextField(
		blank=True, 
		null=True,
		verbose_name='Opiekacz EN'
	)

	grill_pl = models.TextField(
		blank=True, 
		null=True,
		verbose_name='Grill PL'
	)

	grill_en = models.TextField(
		blank=True, 
		null=True,
		verbose_name='Grill EN'
	)

	toster_pl = models.TextField(
		blank=True, 
		null=True,
		verbose_name='Toster  PL'
	)

	toster_en = models.TextField(
		blank=True, 
		null=True,
		verbose_name='Toster  PL'
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

	
	def get_absolute_url(self):
		return reverse('news:news_detail', kwargs={'slug': self.slug, })

	def getlistArticle(self):		
		return Product.objects.all()

	@classmethod
	def getBestSeller(cls):
		return Product.objects.filter(best_seller=True)[:4]

	def thumbnail(self):
  		return mark_safe(
  			'<img width="40" height="40" src="/media/{}" />'.format(
  				self.product_mini_file))

  	def __str__(self):
  		return self.name_pl

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



 	
 		 
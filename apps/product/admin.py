from django.contrib import admin
from .models import LogisticData, Product
from cms.admin.placeholderadmin import PlaceholderAdminMixin
# Register your models here.


class LogisticDataAdmin(admin.ModelAdmin):
	list_display = ['product_name_pl','Logistic_data']

admin.site.register(LogisticData, LogisticDataAdmin)

class ProductAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
	list_display = ['thumbnail', 'name_pl','category', 'best_seller']
	list_filter = ('category','best_seller')
	search_fields = ('name_pl', 'name_en')

admin.site.register(Product, ProductAdmin)
		
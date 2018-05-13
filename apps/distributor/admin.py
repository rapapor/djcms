from django.contrib import admin
from .models import Distributor
from cms.admin.placeholderadmin import PlaceholderAdminMixin

# Register your models here.
class DistributorAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
	list_display = ['biz_name_pl','active']
	

admin.site.register(Distributor, DistributorAdmin)

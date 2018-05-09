from django.contrib import admin
from .models import JobOffer
from cms.admin.placeholderadmin import PlaceholderAdminMixin
# Register your models here.


def active_offer(ModelAdmin, request, queryset):
	queryset.update(active=True)
active_offer.short_description = 'Aktywuj ogloszenie'

def unactive_offer(ModelAdmin, request, queryset):
	queryset.update(active=False)
unactive_offer.short_description = 'Deaktywuj ogloszenie'

class JobOfferAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
	list_display = ['position_pl', 'city','pub_date', 'active']
	list_filter = ('position_pl','city', 'active')
	search_fields = ('position_pl', 'city')
	actions = [active_offer,unactive_offer]

admin.site.register(JobOffer, JobOfferAdmin)
		
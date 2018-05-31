# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Contact
from cms.admin.placeholderadmin import PlaceholderAdminMixin

# Register your models here.
class ContactAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
	list_display = ['name_pl','position_pl','active']
	

admin.site.register(Contact, ContactAdmin)

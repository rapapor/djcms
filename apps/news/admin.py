from django.contrib import admin
from .models import News
from cms.admin.placeholderadmin import PlaceholderAdminMixin

# Register your models here.
class NewsAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
	list_display = ['title_pl','pub_date']
	prepopulated_fields = {"slug": ("title_pl",)}


admin.site.register(News, NewsAdmin)
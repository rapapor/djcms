from django.contrib import admin
from .models import News

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
	list_display = ['title_pl','pub_date']
	prepopulated_fields = {"slug": ("title_pl",)}


admin.site.register(News, NewsAdmin)
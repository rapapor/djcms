from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import News


@plugin_pool.register_plugin
class LastNews(CMSPluginBase):
    render_template = "last_news.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(LastNews, self).render(context, instance, placeholder)
        context['last_news'] = News.getLastNews()        
        return context
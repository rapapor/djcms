from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import Product, LogisticData


@plugin_pool.register_plugin
class BestSeller(CMSPluginBase):
    render_template = "best_seller.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(BestSeller, self).render(context, instance, placeholder)
        context['moja_list'] = Product.getBestSeller()
        return context


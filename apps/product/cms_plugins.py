from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import LogisticData, Product


@plugin_pool.register_plugin
class BestSeller(CMSPluginBase):
    render_template = "best_seller.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(BestSeller, self).render(context, instance, placeholder)
        context['moja_list'] = Product.getBestSeller()
        return context
        

@plugin_pool.register_plugin    
class RandomProduct(CMSPluginBase):
    render_template = "random_product.html"
    cache = False

    def render(self, context, instance, placeholder):		
        context = super(RandomProduct, self).render(context, instance, placeholder)
        context['random'] = Product.getRandomProduct()
        return context

	   
       
	   
       
        
# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _



class ProductApp(CMSApp):
	name = _('Product')
	app_name = 'Product'
	

	def get_urls(self, page=None, language=None, **kwargs):
		return ["apps.product.urls"]


apphook_pool.register(ProductApp)
		
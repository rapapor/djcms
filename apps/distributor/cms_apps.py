from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _



class DistributorApp(CMSApp):
	name = _('Distributor')
	app_name = 'Distributor'
	

	def get_urls(self, page=None, language=None, **kwargs):
		return ["apps.distributor.urls"]


apphook_pool.register(DistributorApp)
		
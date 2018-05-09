from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _



class JobOfferApp(CMSApp):
	name = _('JobOffer')
	app_name = 'JobOffer'
	

	def get_urls(self, page=None, language=None, **kwargs):
		return ["apps.job.urls"]


apphook_pool.register(JobOfferApp)
		
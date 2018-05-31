# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _



class ContactApp(CMSApp):
	name = _('Contact')
	app_name = 'Contact'
	

	def get_urls(self, page=None, language=None, **kwargs):
		return ["apps.contact.urls"]


apphook_pool.register(ContactApp)
		
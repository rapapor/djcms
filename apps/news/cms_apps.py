from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from .menu import NewsSubMenu


class NewsApp(CMSApp):
	name = _('News')
	app_name = 'news'
	menus = [NewsSubMenu,]

	def get_urls(self, page=None, language=None, **kwargs):
		return ["apps.news.urls"]


apphook_pool.register(NewsApp)
		
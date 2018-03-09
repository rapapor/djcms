from django.utils.translation import ugettext_lazy as _ 
from django.utils.safestring import mark_safe
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu

from .models import News


class NewsSubMenu(CMSAttachMenu):
	
	name = _("News Sub-Menu")

	def get_nodes(self, request):

		nodes = []

		for news in News.objects.order_by('title_pl').all():
			node = NavigationNode(
				mark_safe(news.title_pl),
				news.get_absolute_url(),
				news.id,
				)


			nodes.append(node)

		return nodes



menu_pool.register_menu(NewsSubMenu)
	
		
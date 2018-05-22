# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar.items import Break
from cms.cms_toolbars import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK
from cms.toolbar_base import CMSToolbar



@toolbar_pool.register
class ProductToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, _('Rudopal Apps'))
        position = admin_menu.find_first(Break, identifier=ADMINISTRATION_BREAK)
        menu = admin_menu.get_or_create_menu('Produkt', _('Produkty'), position=position)
        url = reverse('admin:product_product_changelist')
        menu.add_sideframe_item(_('Produkty'), url=url)
        url2 = reverse('admin:product_logisticdata_changelist')
        menu.add_sideframe_item(_('Dane logistyczne'), url=url2)
        admin_menu.add_break('product-break', position=menu)



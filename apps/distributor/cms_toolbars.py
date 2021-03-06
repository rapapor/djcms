# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar.items import Break
from cms.cms_toolbars import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK
from cms.toolbar_base import CMSToolbar



@toolbar_pool.register
class Distributor(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, _('Rudopal Apps'))
        position = admin_menu.find_first(Break, identifier=ADMINISTRATION_BREAK)
        menu = admin_menu.get_or_create_menu('Dystrybutorzy', _('Dystrybutorzy'), position=position)
        url = reverse('admin:distributor_distributor_changelist')
        menu.add_sideframe_item(_('Dystrybutorzy'), url=url)
        admin_menu.add_break('dist-break', position=menu)



# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class InheritSaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Inherit Sale Order'


    def sale_list_view_button(self):
        print('sale_list_view_button>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        return True
# -*- coding: utf-8 -*-


from odoo import models, fields, api, _

class InheritPurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    _description = 'Inherit Purchase Order'


    def purchase_list_view_button(self):
        print('purchase_list_view_button>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
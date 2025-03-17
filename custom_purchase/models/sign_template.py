# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SignTemplate(models.Model):
    _inherit = 'sign.template'

    purchase_order_id = fields.Many2one("purchase.order")

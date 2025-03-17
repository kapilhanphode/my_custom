# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import base64
from odoo.exceptions import ValidationError, UserError


class PurchaseOrderSignWizard(models.TransientModel):
    _name = 'purchase.order.sign.wizard'
    _description = 'Purchase Order Sign Wizard'

    report_id = fields.Many2one('ir.actions.report', string='Report', domain=[('model', '=', 'purchase.order')])


    def action_sign_report(self):
        print('action_sign_report>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        active_id = self._context.get('active_id')
        if not active_id or not self.report_id:
            return
        print('active_id>>>>>>>>>>>>>>>>>>>',active_id)

        po_id = self.env['purchase.order'].browse(active_id)
        xml_str = self.report_id._render_qweb_pdf(self.report_id.report_name, po_id.ids)

        # Create a unique name for the report
        report_name = 'Signed_' + po_id.name + po_id.partner_id.name
        template_name = report_name + '/' + self.report_id.name.split('/')[-1]

        # Create an attachment for the report
        attachment_id = self.env['ir.attachment'].create({
            'name': template_name,
            'type': 'binary',
            'datas': base64.b64encode(xml_str[0]),
            'res_model': 'purchase.order',
            'res_id': po_id.id,
        })

        tag_id = self.env['sign.template.tag'].search([('name', '=', self.report_id.name)], limit=1)
        if not tag_id:
            tag_id = self.env['sign.template.tag'].create({'name': self.report_id.name})

        folder = self.env['documents.folder'].search([], limit=1)
        if not folder:
            raise UserError(_("No document folder found. Please create a folder first."))
        doc_id = self.env['documents.document'].create({
            'name': _("Sign \"%(name)s\"") % {'name': attachment_id.name},
            'attachment_id': attachment_id.id,
            'res_model': 'purchase.order',
            'res_id': po_id.id,
            'folder_id': folder.id,
        })

        # Create a sign template and attach it to the purchase.requisition record
        sign_template = po_id.sign_template_ids.create({
            'attachment_id': attachment_id.id,
            'purchase_order_id': po_id.id,
            'tag_ids': [(6, 0, tag_id.ids)]

        })

        # Return action to open the sign interface
        return {
            'name': _("Sign \"%(name)s\"") % {'name': attachment_id.name},
            'type': 'ir.actions.client',
            'tag': 'sign.Template',
            'params': {
                'id': sign_template.id,
                'sign_directly_without_mail': False,
            },
        }

# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class InheritPurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    _description = 'Inherit Purchase Order'

    sign_template_ids = fields.One2many('sign.template', 'purchase_order_id')
    # all_templates_signed = fields.Boolean(compute='_compute_all_templates_signed')

    login_user_manager = fields.Many2one('hr.employee', string='Login User')  # compute = "_is_compute_manager"
    is_manager = fields.Boolean(string="Is Manager", compute='_is_manager')


    def open_sign_document_wizard(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _("SIGN PO"),
            'res_model': 'purchase.order.sign.wizard',
            'target': 'new',
            'view_mode': 'form',
            # 'domain': [('id', 'in', self.tax_cash_basis_created_move_ids.ids)],
            # 'views': [(self.env.ref('account.view_move_tree').id, 'tree'), (False, 'form')],
        }

    def purchase_list_view_button(self):
        '''Added button on list view of purchase order
            Visible: on selecting record from list view'''
        print('purchase_list_view_button>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

    def create(self, vals):
        res = super().create(vals)
        res.login_user_manager = self.env['hr.employee'].search([('user_id', '=', self.env.user.id)],
                                                                limit=1).parent_id.id
        return res

    def write(self, vals):
        vals['login_user_manager'] = self.env['hr.employee'].search([('user_id', '=', self.env.user.id)],
                                                                    limit=1).parent_id.id
        return super().write(vals)

    def _is_manager(self):
        for rec in self:
            login_user_manager_id = self.env['hr.employee'].search([('user_id', '=', self.env.user.id)])
            if rec.login_user_manager == login_user_manager_id:
                rec.is_manager = True
            else:
                rec.is_manager = False

    @api.model
    def retrieve_dashboard(self):
        res = super(InheritPurchaseOrder, self).retrieve_dashboard()
        print('Custom retrieve_dashboard>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        po = self.env['purchase.order']
        res['all_cancel'] = po.search_count([('state', '=', 'cancel')])
        res['my_cancel'] = po.search_count([('state', '=', 'cancel'), ('user_id', '=', self.env.uid)])

        return res

    # def _is_compute_manager(self):
    #     # tried with compute method but this does not store the value or it not working as per expectations
    #     user_id = self.env.user
    #     # print('user_id.employee_id>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',user_id.employee_id)
    #     for rec in self:
    #         print('rec..........................',rec.login_user_manager)
    #         employee_id = rec.env['hr.employee'].search([('user_id', '=', user_id.id)])
    #         print('manager_id...............................',employee_id.parent_id)
    #         rec.login_user_manager = employee_id.parent_id.id

    '''login_user_manager : On create or update recorde(PO) this filed will store the manager of login employee
    is_manager : If the login employee is the manager of PO created employee then it will return true'''

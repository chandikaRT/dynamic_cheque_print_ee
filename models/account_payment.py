from odoo import models, fields,api

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    Cheque_number = fields.Char(string='Cheque Number')

    @api.model
    def _get_next_cheque_number(self):
        company_id = self.env.company.id
        last_cheque = self.search([('company_id', '=', company_id)], order='id desc', limit=1)
        if last_cheque and last_cheque.cheque_number:
            return str(int(last_cheque.cheque_number) + 1)
        else:
            return '1'

    @api.model
    def create(self, vals):
        if vals.get('cheque_number') is None:
            vals['cheque_number'] = self._get_next_cheque_number()
        return super(AccountPayment, self).create(vals)

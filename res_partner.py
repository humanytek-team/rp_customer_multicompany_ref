# -*- coding: utf-8 -*-

from openerp import models, fields, api, _

class res_partner(models.Model):
	_inherit = 'res.partner'

	partner_company_ref = fields.Char(
        'Referencia de Empresa', company_dependent=True,
        groups="base.group_user",
        help="Referencia con la que el cliente reconoce a la empresa emisora de la factura.")

	#partner_company_ref = fields.One2many('res.partner.company.ref', 'name', string='Referencia por Empresa')


# class res_partner_company_ref(models.Model):
# 	_name = 'res.partner.company.ref'

# 	name = fields.Integer('Id', size=64)
# 	company_id = fields.Many2one('res.company', 'Empresa', ondelete='cascade', required=True)
# 	reference = fields.Char(string="Referencia")
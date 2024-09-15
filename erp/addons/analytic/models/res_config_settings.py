# -*- coding: utf-8 -*-
# Part of ERP. See LICENSE file for full copyright and licensing details.

from erp import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_analytic_accounting = fields.Boolean(string='Analytic Accounting', implied_group='analytic.group_analytic_accounting')

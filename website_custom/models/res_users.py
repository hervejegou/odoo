# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    tags = fields.Char(string='Tags',
                       export_string_translation=False,
                       help="Comma-separated list of tags for the user",
                       copy=False)
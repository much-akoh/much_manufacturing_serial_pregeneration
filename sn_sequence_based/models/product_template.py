# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_serial_id = fields.Many2one(
        comodel_name="product.serial.number", string="Serial Number Sequence"
    )

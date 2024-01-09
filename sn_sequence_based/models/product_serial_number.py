# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ProductSerialNumber(models.Model):
    _name = "product.serial.number"
    _inherits = {"ir.sequence": "sequence_id"}
    _description = "Serial Number Circles"

    product_ids = fields.One2many(
        comodel_name="product.template",
        inverse_name="product_serial_id",
        compute="_compute_product_ids",
        string="Products",
    )
    sequence_id = fields.Many2one(
        "ir.sequence",
        "Sequence",
        auto_join=True,
        index=True,
        ondelete="cascade",
        required=True,
    )

    def _compute_product_ids(self):
        for rec in self:
            rec.product_ids = self.env["product.template"].search(
                [("product_serial_id", "=", rec.id)]
            )

    @api.model
    def next_by_code(self, product_serial, sequence_date=None):
        """
        Draw an interpolated string using a sequence with the requested code.
        If several sequences with the correct code are available to the user
        (multi-company cases), the one from the user's current company will
        be used.
        """
        self.check_access_rights("read")
        if not product_serial or not product_serial.code:
            raise ValidationError(
                _(
                    "No sequence has been found for code '%s'."
                    " Please make sure a sequence is set for current company."
                    % product_serial.code
                )
            )
        if product_serial.padding < len(str(product_serial.number_next_actual)):
            raise ValidationError(
                _(
                    "The serial number size was bigger than"
                    " the specified sequence size."
                )
            )
        return product_serial.sequence_id._next(sequence_date=sequence_date)

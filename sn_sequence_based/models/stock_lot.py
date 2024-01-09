# -*- coding: utf-8 -*-

from odoo import _, api, models
from odoo.exceptions import ValidationError


class StockLot(models.Model):
    _inherit = "stock.lot"

    @api.constrains("name", "company_id")
    def _check_unique_lot_number(self):
        domain = [
            ("company_id", "in", self.company_id.ids),
            ("name", "in", self.mapped("name")),
        ]
        fields = ["company_id", "name"]
        groupby = ["company_id", "name"]
        records = self.read_group(domain, fields, groupby, lazy=False)
        error_message_lines = []
        for rec in records:
            if rec["__count"] > 1:
                error_message_lines.append(
                    _(" - Product Serial Number: %s", rec["name"])
                )
        if error_message_lines:
            raise ValidationError(
                _(
                    "The combination of serial number and product must be unique across"
                    " a company.\nFollowing combination contains duplicates:\n"
                )
                + "\n".join(error_message_lines)
            )

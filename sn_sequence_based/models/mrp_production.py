# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.exceptions import ValidationError


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    lot_ids = fields.Many2many("stock.lot", string="Serial Numbers", copy=False)

    def _prepare_stock_lot_values(self):
        """
        Override the method to generate a product serial sequence
        :return:
        """
        self.ensure_one()
        name = self.env["product.serial.number"].next_by_code(
            self.product_id.product_tmpl_id.product_serial_id
        )
        return {
            "product_id": self.product_id.id,
            "company_id": self.company_id.id,
            "name": name,
        }

    def button_generate_serial_numbers(self):
        self.ensure_one()
        if self.product_tmpl_id.product_serial_id and self.product_qty:
            self.write(
                {
                    "lot_ids": [
                        (0, 0, self._prepare_stock_lot_values())
                        for i in range(0, int(self.product_qty))
                    ]
                }
            )
        else:
            raise ValidationError(
                'Please first set a "Serial Number Sequence" on the Product.'
            )

    def _split_productions(
        self, amounts=False, cancel_remaining_qty=False, set_consumed_qty=False
    ):
        res = super()._split_productions(
            amounts, cancel_remaining_qty, set_consumed_qty
        )
        lot_ids = False
        for rec in res:
            if rec.id == self.id and self.lot_producing_id and self.lot_ids:
                lot_ids = self.lot_ids - self.lot_producing_id
            if rec.id != self.id and lot_ids:
                rec.write({"lot_ids": [(6, 0, lot_ids.ids)]})
        return res

# -*- coding: utf-8 -*-
from odoo import fields, models
from re import findall as regex_findall


class StockAssignSerialNumbers(models.TransientModel):
    _inherit = "stock.assign.serial"

    next_serial_number = fields.Char(required=False)

    def generate_serial_numbers_production(self):
        """
        Override the method to manage a sequence
        :return:
        """
        product = self.production_id.product_id.product_tmpl_id
        next_serial_number = self.env["product.serial.number"].next_by_code(
            product.product_serial_id
        )
        if next_serial_number and self.next_serial_count:
            generated_serial_numbers = "\n".join(
                self.env["stock.lot"].generate_lot_names(
                    next_serial_number, self.next_serial_count
                )
            )
            self.serial_numbers = (
                "\n".join([self.serial_numbers, generated_serial_numbers])
                if self.serial_numbers
                else generated_serial_numbers
            )
            self._onchange_serial_numbers()
            caught_initial_number = regex_findall(r"\d{1,}$", self.serial_numbers)
            caught_initial_number = int(caught_initial_number[-1]) + 1
            product.product_serial_id.sequence_id.update(
                {"number_next_actual": caught_initial_number}
            )
        action = self.env["ir.actions.actions"]._for_xml_id(
            "mrp.act_assign_serial_numbers_production"
        )
        action["res_id"] = self.id
        return action

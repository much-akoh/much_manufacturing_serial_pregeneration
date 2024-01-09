# sn_sequence_based

Product serial sequence number 
**Table of Contents**

- Features & Limitations
- Configuration
- Usage
- Issues & Bugs
- Development
- Tests
- Dependencies

---

## Features

- Extend the ir sequence view to add new fields.
- Add field on product template


---

## Configuration
- Manage Product base sequence number
---

## Usage
- 

---

## Dependencies

### Odoo modules dependencies

| Module  | Why used?                                   | Side effects   |
|---------|---------------------------------------------| -------------- |
| base    | To exted the sequence view                  | No side effect |
| mrp     | To make modification in sequence generation | No side effect |



### Python library dependencies

The module doesn't require any external Python library

---

## Limitations, Issues & Bugs

The module doesn't require any Limitations, Issues & Bugs

---

## Development

1. Extend `sequence_view` view of **ir.sequence**
2. Add fields `product_ids` and `sequence_id` on **product.serial.number**                                                                                         Add field `product_serial_id` on **product.template**
3. Add field `product_serial_id` on **product.template**
4. Extend method `next_by_code` to modify sequence generation of **ir.sequence**
5. Override method `_prepare_stock_lot_values` to modify sequence generation of **mrp.production** 
6. Override method `generate_serial_numbers_production` to modify sequence generation of **stock.assign.serial**
7. Add method `_check_unique_lot_number` on **stock.lot** 
---

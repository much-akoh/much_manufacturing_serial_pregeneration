# -*- coding: utf-8 -*-
{
    "name": "Sequence Serial Numbers",
    "summary": """ Sequence Serial Numbers """,
    "description": """Module for sequence serial Numbers""",
    "author": "much. GmbH",
    "website": "https://muchconsulting.de/",
    "version": "17.0.1.0.0",
    "depends": ["mrp"],
    "data": [
        "security/ir.model.access.csv",
        "views/product_serial_number_view.xml",
        "views/product_template_view_inherit.xml",
        "views/mrp_production_views.xml",
        "wizard/stock_assign_serial_numbers.xml",
    ],
    "application": False,
    "installable": True,
    "auto_install": False,
    "license": "Other proprietary",
}

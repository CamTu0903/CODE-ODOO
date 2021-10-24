# -*- coding: utf-8 -*-
{
    'name': "Phone",
    'summary': """ Phone model""",
    'description': """Managing phone information""",
    'author': "Cam Tu",
    'website': "https://www.odoo.com/page/billing",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/returns.xml',
        'views/product.xml',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': True,
}
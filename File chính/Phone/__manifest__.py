# -*- coding: utf-8 -*-
{
    'name': "Phone",
    'summary': """ Phone model""",
    'description': """Managing phone information""",
    'author': "Cam Tu",
    'website': "https://www.odoo.com/page/billing",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['product','sale','stock_account'],
    'data': [
        'security/ir.model.access.csv',
        'views/returns.xml',
        'views/brand.xml',
        'views/product_template.xml',
        'views/brand_models.xml',
        'views/hoadon.xml',
        'views/invoices.xml',
        'views/warranty.xml',
        'views/gift.xml',
        'views/branch.xml',
        'views/ncc.xml',
        'views/nvc.xml',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': True,
}
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
        # 'views/product.xml',
        'views/brand.xml',
        'views/product_template.xml',
        'views/brand_models.xml',
        'views/hoadon.xml',
        'views/invoices.xml',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': True,
}
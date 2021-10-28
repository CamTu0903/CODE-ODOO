# -*- coding: utf-8 -*-
{
    'name': "Dienthoai",
    'summary': """ Phone model""",
    'description': """Managing phone information""",
    'author': "Cam Tu",
    'website': "https://www.odoo.com/page/billing",
    'category': 'Uncategorized',
    'version': '0.1',
    'sequence': -150,
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        # 'data/doitradata.xml',
        'data/returnsdata.xml',
        'data/productdata.xml',
        'views/doitra.xml',
        'views/returns.xml',
        'views/product.xml',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': True,
}
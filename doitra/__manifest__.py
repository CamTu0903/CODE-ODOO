# -*- coding: utf-8 -*-
{
    'name': "Module Đổi Trả",
    'summary': """ Shoes management""",
    'description': """


    """,
    'website': "ThuHoai.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'sequence': -150,
    'author': "",

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

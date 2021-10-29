{
    'name': 'Phone_Shop_module',
    'version': '1.0',
    'sequence': -100,
    'author': 'nguyen_thi_kim_oanh',
    'website': '',
    'summary': '',
    'description': '',
    'category': 'Industries',
    'depends': [
        'base', 'stock_account', 'mail', 'product', 'account'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/phone_view.xml',

    ],
    'demo': [],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
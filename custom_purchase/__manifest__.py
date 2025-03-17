{
    'name': "Custom Purchase - Kapil",
    'version': '1.0.2',
    'author': 'Kapil',
    'website': '',
    'category': 'Purchase',
    'license': 'LGPL-3',
    'depends': ['base', 'purchase', 'hr', 'sign', 'documents'],
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_order_view.xml',
        'wizard/purchase_order_sign_wizard.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_purchase/static/src/xml/**',
            # 'custom_purchase/static/src/js/**',
        ],
    },
    'installable': True,
    'application': True,
}

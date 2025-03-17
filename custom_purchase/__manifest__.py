{
    # =========================
    # Module Information
    # =========================
    'name': "Custom Purchase - Kapil",
    'version': '17.0.1.0.2',
    'category': 'Purchase Module Customization',
    'summary': 'Enhancements to the base Odoo Purchase module, including signing and improved UI.',
    'description': """
        This module extends the functionality of the standard Odoo Purchase module 
        by adding new features such as digital signing, an improved purchase order view and etc,.
    """,

    # =========================
    # Author & Maintenance
    # =========================
    'author': 'Kapil',
    'maintainer': 'Kapil',
    'website': '',

    # =========================
    # Dependencies
    # =========================
    'depends': [
        'base',
        'purchase',
        'hr',
        'sign',
        'documents'
    ],

    # =========================
    # Data Files
    # =========================
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_order_view.xml',
        'wizard/purchase_order_sign_wizard.xml',
    ],

    # =========================
    # Assets
    # =========================
    'assets': {
        'web.assets_backend': [
            'custom_purchase/static/src/xml/**',
        ],
    },

    # =========================
    # Technical Information
    # =========================
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

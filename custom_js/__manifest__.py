{
    'name': "Custom Js - Kapil",
    'version': '1.0.2',
    'author': 'Kapil',
    'website': '',
    'category': 'Js',
    'license': 'LGPL-3',
    'depends': ['sale_management'],
    'data': [    
        'views/button_list_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_js/static/src/js/**',
            'custom_js/static/src/xml/**',
        ],
    },
    'installable': True,
    'application': True,
}
#
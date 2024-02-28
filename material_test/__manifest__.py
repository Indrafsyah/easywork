{
        'name': 'Material & Supplier',
        'version': '16.0.1.0',
        'category': 'Tools',
        'summary': 'Material management module',
        'description': """
            This module manages materials & suppliers.
        """,
        'author': 'aditya nugraha',
        'depends': ['base'],
        'data': [
            'views/material_menu.xml',
            'security/ir.model.access.csv',
            
        ],
        'application': True,
        'installable': True,
        'auto_install': False,
        'sequence': 2,
        'license': 'LGPL-3',
}
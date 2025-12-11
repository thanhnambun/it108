# -*- coding: utf-8 -*-
{
    'name': 'Estate Management',
    'version': '1.0',
    'category': 'Real Estate',
    'summary': 'Quản lý bất động sản và khách hàng',
    'description': """
        Estate Management Module
        ========================
        Module quản lý bất động sản với các tính năng:
        - Quản lý khách hàng (Customer)
        - Quản lý bất động sản (EstateProperty)
        - Quan hệ Many2one: Property -> Customer
        - Quan hệ One2many: Customer -> Properties
    """,
    'author': 'Donut',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_views.xml',
        'views/estate_property_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

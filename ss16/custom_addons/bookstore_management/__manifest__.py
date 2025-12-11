# -*- coding: utf-8 -*-
{
    'name': 'Bookstore Management',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Quản lý cửa hàng sách',
    'description': """
        Bookstore Management Module
        ============================
        Module quản lý cửa hàng sách với các chức năng:
        - Quản lý thông tin sách
        - Theo dõi tác giả, giá, ngày xuất bản
        - Kết nối với PostgreSQL thông qua Odoo ORM
    """,
    'author': 'Donut',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

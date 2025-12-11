# -*- coding: utf-8 -*-
{
    'name': 'Product Management',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Quản lý sản phẩm',
    'description': """
        Product Management Module
        =========================
        Module quản lý sản phẩm với các trường dữ liệu cơ bản:
        - Tên sản phẩm (Char)
        - Giá sản phẩm (Float)
        - Số lượng sản phẩm (Integer)
    """,
    'author': 'Donut',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

# -*- coding: utf-8 -*-
{
    'name': 'Real Estate',
    'version': '1.0',
    'category': 'Real Estate',
    'summary': 'Quản lý bất động sản',
    'description': """
        Real Estate Management
        ======================
        Module quản lý bất động sản với đầy đủ thông tin:
        - Thông tin cơ bản: tên, mô tả, mã bưu điện, ngày mở bán, giá
        - Chi tiết căn nhà: phòng ngủ, diện tích, mặt tiền, gara, vườn
    """,
    'author': 'Donut',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/property_views.xml',
    ],
    'demo': [
        'demo/demo_properties.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

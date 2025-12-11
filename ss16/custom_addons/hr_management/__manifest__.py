# -*- coding: utf-8 -*-
{
    'name': 'HR Management',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Quản lý nhân sự',
    'description': """
        HR Management Module
        ====================
        Module quản lý nhân sự với các tính năng:
        - Quản lý thông tin nhân viên
        - Theo dõi trạng thái làm việc (Selection field)
        - Quản lý email, số điện thoại, ngày vào làm
    """,
    'author': 'Donut',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

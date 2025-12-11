# -*- coding: utf-8 -*-
{
    'name': 'Revenue Management',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Quản lý doanh thu',
    'description': """
        Revenue Management Module
        =========================
        Module quản lý doanh thu với các tính năng:
        - Thêm mới doanh thu
        - Cập nhật thông tin doanh thu
        - Tính tổng doanh thu theo ngày/khoảng thời gian
        - Báo cáo và thống kê
    """,
    'author': 'Donut',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/revenue_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

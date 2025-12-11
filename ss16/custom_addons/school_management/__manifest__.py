# -*- coding: utf-8 -*-
{
    'name': 'School Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Quản lý trường học, học viên và kỳ thi',
    'description': """
        School Management System
        ========================
        Module quản lý giáo dục với PostgreSQL:
        - Quản lý trường học (School)
        - Quản lý học viên (Student)
        - Quản lý kỳ thi (Exam)
        - Quan hệ Many2one: Student -> School, Exam -> School
        - Quan hệ Many2many: Exam <-> Students
        - CRUD operations đầy đủ
        - Tính điểm trung bình
    """,
    'author': 'Donut',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/school_views.xml',
        'views/student_views.xml',
        'views/exam_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

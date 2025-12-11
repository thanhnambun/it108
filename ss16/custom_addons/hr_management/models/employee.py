# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Employee(models.Model):
    _name = 'hr.employee.management'
    _description = 'Employee Management'
    _rec_name = 'name'  # Sử dụng 'name' làm tên hiển thị

    # Trường name (theo yêu cầu mới)
    name = fields.Char(
        string='Tên nhân viên',
        required=True,
        help='Nhập tên nhân viên'
    )
    
    # Trường position với Selection (theo yêu cầu mới)
    position = fields.Selection(
        selection=[
            ('manager', 'Quản lý'),
            ('developer', 'Lập trình viên'),
            ('designer', 'Thiết kế'),
            ('accountant', 'Kế toán'),
            ('hr', 'Nhân sự'),
            ('sales', 'Kinh doanh'),
            ('marketing', 'Marketing')
        ],
        string='Vị trí',
        required=True,
        help='Chọn vị trí công việc'
    )
    
    # Trường salary với default=1000 (theo yêu cầu mới)
    salary = fields.Float(
        string='Lương (VNĐ)',
        default=1000,
        required=True,
        help='Mức lương của nhân viên',
        digits=(16, 2)
    )
    
    # Trường start_date với default=today (theo yêu cầu mới)
    start_date = fields.Date(
        string='Ngày bắt đầu',
        default=fields.Date.today,
        required=True,
        help='Ngày bắt đầu làm việc'
    )
    
    # Các trường bổ sung
    employee_status = fields.Selection(
        selection=[
            ('active', 'Đang làm việc'),
            ('inactive', 'Nghỉ việc'),
            ('on_leave', 'Đang nghỉ phép'),
            ('probation', 'Thử việc')
        ],
        string='Trạng thái',
        required=True,
        default='active',
        help='Chọn trạng thái của nhân viên'
    )
    
    employee_email = fields.Char(
        string='Email',
        help='Email của nhân viên'
    )
    
    employee_phone = fields.Char(
        string='Số điện thoại',
        help='Số điện thoại liên lạc'
    )
    
    # Trường tính toán: số năm làm việc
    years_of_service = fields.Integer(
        string='Số năm làm việc',
        compute='_compute_years_of_service',
        store=True,
        help='Số năm làm việc tính từ ngày bắt đầu'
    )
    
    @api.depends('start_date')
    def _compute_years_of_service(self):
        """Tính số năm làm việc từ start_date đến hiện tại"""
        from datetime import date
        for record in self:
            if record.start_date:
                today = date.today()
                delta = today - record.start_date
                record.years_of_service = delta.days // 365
            else:
                record.years_of_service = 0

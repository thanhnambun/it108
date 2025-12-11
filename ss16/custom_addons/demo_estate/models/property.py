# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'demo.estate.property'
    _description = 'Real Estate Property'
    _rec_name = 'name'
    _order = 'date_availability desc'

    
    name = fields.Char(
        string='Tên tài sản',
        required=True,
        help='Đây là tiêu đề hiển thị chính của bất động sản'
    )
    
    description = fields.Text(
        string='Mô tả',
        help='Dùng để viết bài giới thiệu chi tiết, dài nhiều dòng'
    )
    
    postcode = fields.Char(
        string='Mã bưu điện',
        help='Lưu mã ZIP code của khu vực'
    )
    
    date_availability = fields.Date(
        string='Ngày mở bán',
        default=fields.Date.today,
        copy=False,
        help='Mặc định lấy ngày hiện tại khi tạo mới. Không được sao chép khi nhân bản (Duplicate)'
    )
    
    expected_price = fields.Float(
        string='Giá mong muốn',
        required=True,
        digits=(16, 2),
        help='Bắt buộc nhập. Giá mà người bán kỳ vọng'
    )
    
    selling_price = fields.Float(
        string='Giá bán thực tế',
        readonly=True,
        copy=False,
        digits=(16, 2),
        help='Chỉ đọc (Read-only). Người dùng không được sửa tay. Không được sao chép khi nhân bản'
    )
    
    
    bedrooms = fields.Integer(
        string='Số phòng ngủ',
        default=2,
        help='Mặc định là 2 phòng'
    )
    
    living_area = fields.Integer(
        string='Diện tích ở',
        help='Đơn vị: mét vuông (m²)'
    )
    
    facades = fields.Integer(
        string='Số mặt tiền',
        help='Số lượng mặt tiền của căn nhà'
    )
    
    garage = fields.Boolean(
        string='Có Gara xe?',
        help='Đánh dấu nếu nhà có chỗ để xe'
    )
    
    garden = fields.Boolean(
        string='Có vườn?',
        help='Đánh dấu nếu nhà có sân vườn'
    )
    
    garden_area = fields.Integer(
        string='Diện tích vườn',
        help='Đơn vị: mét vuông (m²)'
    )
    
    garden_orientation = fields.Selection(
        selection=[
            ('north', 'Bắc'),
            ('south', 'Nam'),
            ('east', 'Đông'),
            ('west', 'Tây')
        ],
        string='Hướng vườn',
        help='Danh sách chọn có định: Bắc, Nam, Đông, Tây'
    )
    
    total_area = fields.Integer(
        string='Tổng diện tích',
        compute='_compute_total_area',
        store=True,
        help='Tổng diện tích = Diện tích ở + Diện tích vườn'
    )
    
    active = fields.Boolean(
        string='Đang bán',
        default=True
    )
    
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = (record.living_area or 0) + (record.garden_area or 0)
    
    @api.constrains('expected_price')
    def _check_expected_price(self):
        for record in self:
            if record.expected_price <= 0:
                raise ValidationError('Giá mong muốn phải lớn hơn 0!')
    
    @api.constrains('selling_price')
    def _check_selling_price(self):
        for record in self:
            if record.selling_price < 0:
                raise ValidationError('Giá bán không thể âm!')
    
    @api.onchange('garden')
    def _onchange_garden(self):
        """Khi bỏ chọn vườn, reset diện tích và hướng vườn"""
        if not self.garden:
            self.garden_area = 0
            self.garden_orientation = False

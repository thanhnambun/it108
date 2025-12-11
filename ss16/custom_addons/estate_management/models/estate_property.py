# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class EstateProperty(models.Model):
    """
    Model EstateProperty - Bất động sản
    Mỗi bất động sản thuộc về một khách hàng (Many2one)
    """
    _name = 'estate.property'
    _description = 'Estate Property'
    _rec_name = 'name'

    name = fields.Char(
        string='Tên BĐS',
        required=True,
        help='Tên bất động sản'
    )
    
    description = fields.Text(
        string='Mô tả',
        help='Mô tả chi tiết về bất động sản'
    )
    
    property_type = fields.Selection(
        selection=[
            ('house', 'Nhà ở'),
            ('apartment', 'Căn hộ'),
            ('land', 'Đất'),
            ('villa', 'Biệt thự'),
            ('office', 'Văn phòng'),
            ('warehouse', 'Kho xưởng')
        ],
        string='Loại BĐS',
        required=True,
        default='house',
        help='Loại hình bất động sản'
    )
    
    price = fields.Float(
        string='Giá (VNĐ)',
        required=True,
        default=0.0,
        digits=(16, 2),
        help='Giá bất động sản'
    )
    
    area = fields.Float(
        string='Diện tích (m²)',
        required=True,
        default=0.0,
        help='Diện tích bất động sản'
    )
    
    bedrooms = fields.Integer(
        string='Số phòng ngủ',
        default=0,
        help='Số lượng phòng ngủ'
    )
    
    bathrooms = fields.Integer(
        string='Số phòng tắm',
        default=0,
        help='Số lượng phòng tắm'
    )
    
    address = fields.Char(
        string='Địa chỉ',
        required=True,
        help='Địa chỉ bất động sản'
    )
    
    # Many2one: Mỗi Property thuộc về một Customer
    # Tham số:
    # - 'estate.customer': Model liên kết
    # - ondelete='cascade': Khi xóa Customer, xóa luôn Properties
    customer_id = fields.Many2one(
        comodel_name='estate.customer',
        string='Chủ sở hữu',
        required=True,
        ondelete='cascade',
        help='Khách hàng sở hữu bất động sản này'
    )
    
    # Related field: Lấy thông tin từ customer
    customer_phone = fields.Char(
        string='SĐT chủ sở hữu',
        related='customer_id.phone',
        readonly=True,
        store=True
    )
    
    customer_email = fields.Char(
        string='Email chủ sở hữu',
        related='customer_id.email',
        readonly=True,
        store=True
    )
    
    # Trường tính toán: Giá mỗi m²
    price_per_sqm = fields.Float(
        string='Giá/m²',
        compute='_compute_price_per_sqm',
        store=True,
        digits=(16, 2)
    )
    
    active = fields.Boolean(
        string='Đang bán',
        default=True,
        help='Bỏ chọn nếu đã bán'
    )
    
    @api.depends('price', 'area')
    def _compute_price_per_sqm(self):
        """Tính giá mỗi m²"""
        for record in self:
            if record.area > 0:
                record.price_per_sqm = record.price / record.area
            else:
                record.price_per_sqm = 0.0
    
    @api.constrains('price')
    def _check_price(self):
        """Kiểm tra giá phải > 0"""
        for record in self:
            if record.price <= 0:
                raise ValidationError('Giá bất động sản phải lớn hơn 0!')
    
    @api.constrains('area')
    def _check_area(self):
        """Kiểm tra diện tích phải > 0"""
        for record in self:
            if record.area <= 0:
                raise ValidationError('Diện tích phải lớn hơn 0!')

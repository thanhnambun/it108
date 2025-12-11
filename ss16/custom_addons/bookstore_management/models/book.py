# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Book(models.Model):
    _name = 'bookstore.book'
    _description = 'Book Management'
    _order = 'publish_date desc, title'

    title = fields.Char(
        string='Tên sách',
        required=True,
        help='Nhập tên sách',
        index=True 
    )
    
    author = fields.Char(
        string='Tác giả',
        required=True,
        help='Nhập tên tác giả',
        index=True
    )
    
    price = fields.Float(
        string='Giá sách (VNĐ)',
        required=True,
        default=0.0,
        help='Nhập giá sách',
        digits=(16, 2)  
    )
    
    publish_date = fields.Date(
        string='Ngày xuất bản',
        required=True,
        default=fields.Date.today,
        help='Chọn ngày xuất bản'
    )
    
    isbn = fields.Char(
        string='ISBN',
        help='Mã ISBN của sách'
    )
    
    description = fields.Text(
        string='Mô tả',
        help='Mô tả nội dung sách'
    )
    
    stock_quantity = fields.Integer(
        string='Số lượng tồn kho',
        default=0,
        help='Số lượng sách còn trong kho'
    )
    
    active = fields.Boolean(
        string='Đang kinh doanh',
        default=True,
        help='Bỏ chọn để ngừng kinh doanh sách này'
    )
    
    @api.constrains('price')
    def _check_price(self):
        """Kiểm tra giá sách phải lớn hơn 0"""
        for record in self:
            if record.price < 0:
                raise ValidationError('Giá sách phải lớn hơn hoặc bằng 0!')
    
    @api.constrains('stock_quantity')
    def _check_stock(self):
        """Kiểm tra số lượng tồn kho phải >= 0"""
        for record in self:
            if record.stock_quantity < 0:
                raise ValidationError('Số lượng tồn kho không thể âm!')
    
    _sql_constraints = [
        ('isbn_unique', 'UNIQUE(isbn)', 'Mã ISBN phải là duy nhất!'),
    ]

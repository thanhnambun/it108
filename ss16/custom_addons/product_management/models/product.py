# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Product(models.Model):
    _name = 'product.management'
    _description = 'Product Management'

    product_name = fields.Char(
        string='Tên sản phẩm',
        required=True,
        help='Nhập tên sản phẩm'
    )
    
    product_price = fields.Float(
        string='Giá sản phẩm',
        required=True,
        default=0,
        help='Nhập giá sản phẩm'
    )
    
    product_quantity = fields.Integer(
        string='Số lượng sản phẩm',
        required=True,
        default=0,
        help='Nhập số lượng sản phẩm'
    )

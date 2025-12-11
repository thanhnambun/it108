# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Customer(models.Model):
    """
    Model Customer - Khách hàng
    Một khách hàng có thể sở hữu nhiều bất động sản (One2many)
    """
    _name = 'estate.customer'
    _description = 'Estate Customer'
    _rec_name = 'name'

    name = fields.Char(
        string='Tên khách hàng',
        required=True,
        help='Nhập tên khách hàng'
    )
    
    email = fields.Char(
        string='Email',
        help='Email liên hệ'
    )
    
    phone = fields.Char(
        string='Số điện thoại',
        required=True,
        help='Số điện thoại liên hệ'
    )
    
    address = fields.Text(
        string='Địa chỉ',
        help='Địa chỉ của khách hàng'
    )
    
    # One2many: Một Customer có nhiều Properties
    # Tham số:
    # - 'estate.property': Model liên kết
    # - 'customer_id': Trường Many2one trong model estate.property
    property_ids = fields.One2many(
        comodel_name='estate.property',
        inverse_name='customer_id',
        string='Bất động sản',
        help='Danh sách bất động sản của khách hàng'
    )
    
    # Trường tính toán: Tổng số bất động sản
    property_count = fields.Integer(
        string='Số lượng BĐS',
        compute='_compute_property_count',
        store=True
    )
    
    # Trường tính toán: Tổng giá trị bất động sản
    total_property_value = fields.Float(
        string='Tổng giá trị BĐS',
        compute='_compute_total_property_value',
        store=True,
        digits=(16, 2)
    )
    
    @api.depends('property_ids')
    def _compute_property_count(self):
        """Tính số lượng bất động sản của khách hàng"""
        for record in self:
            record.property_count = len(record.property_ids)
    
    @api.depends('property_ids.price')
    def _compute_total_property_value(self):
        """Tính tổng giá trị bất động sản"""
        for record in self:
            record.total_property_value = sum(record.property_ids.mapped('price'))

from odoo import models, fields


class InventoryProduct(models.Model):
    _name = 'inventory.product'
    _description = 'Inventory Product'

    name = fields.Char(string='Name')
    price = fields.Float(string='Price')
    stock = fields.Integer(string='Stock')

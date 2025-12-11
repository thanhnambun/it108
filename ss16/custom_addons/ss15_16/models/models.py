# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ss15_16(models.Model):
#     _name = 'ss15_16.ss15_16'
#     _description = 'ss15_16.ss15_16'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


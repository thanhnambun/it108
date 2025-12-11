# -*- coding: utf-8 -*-
# from odoo import http


# class Ss1516(http.Controller):
#     @http.route('/ss15_16/ss15_16', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ss15_16/ss15_16/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ss15_16.listing', {
#             'root': '/ss15_16/ss15_16',
#             'objects': http.request.env['ss15_16.ss15_16'].search([]),
#         })

#     @http.route('/ss15_16/ss15_16/objects/<model("ss15_16.ss15_16"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ss15_16.object', {
#             'object': obj
#         })


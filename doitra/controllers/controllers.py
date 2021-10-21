# -*- coding: utf-8 -*-
# from odoo import http


# class Doitra(http.Controller):
#     @http.route('/doitra/doitra/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/doitra/doitra/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('doitra.listing', {
#             'root': '/doitra/doitra',
#             'objects': http.request.env['doitra.doitra'].search([]),
#         })

#     @http.route('/doitra/doitra/objects/<model("doitra.doitra"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('doitra.object', {
#             'object': obj
#         })

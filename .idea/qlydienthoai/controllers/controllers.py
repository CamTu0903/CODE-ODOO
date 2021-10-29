# -*- coding: utf-8 -*-
# from odoo import http


# class Qlydienthoai(http.Controller):
#     @http.route('/qlydienthoai/qlydienthoai/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qlydienthoai/qlydienthoai/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('qlydienthoai.listing', {
#             'root': '/qlydienthoai/qlydienthoai',
#             'objects': http.request.env['qlydienthoai.qlydienthoai'].search([]),
#         })

#     @http.route('/qlydienthoai/qlydienthoai/objects/<model("qlydienthoai.qlydienthoai"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qlydienthoai.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-

from odoo import models, fields, api

class qlydienthoai(models.Model):
    _name = 'qlydienthoai.qlydienthoai'
    _description = 'qlydienthoai.qlydienthoai'

    name = fields.Char("name")
    value = fields.Integer("value")

    description = fields.Text()

class MobileBrand(models.Model):
    _name = 'mobile.brand'
    _rec_name = 'brand_name'

    brand_name = fields.Char(string="Mobile Brand", required=True)

class Gift(models.Model):
    _name = 'gift.mobile'
    _rec_name = 'gift_mobile'

    gift_mobile = fields.Char(string="Gift", required=True)

class PK(models.Model):
    _name = 'pk.mobile'
    _rec_name = 'pk_mobile'

    gift_mobile = fields.Char(string="Phụ kiện", required=True)


#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

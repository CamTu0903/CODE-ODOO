# -*- coding: utf-8 -*-

from odoo import models, fields, api


class qlydienthoai(models.Model):
    _name = 'qlydienthoai.qlydienthoai'
    _description = 'qlydienthoai.qlydienthoai'

    name = fields.Char("name")
    value = fields.Integer("value")

    description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

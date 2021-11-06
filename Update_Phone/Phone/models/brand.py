from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class MobileBrand(models.Model):
    _name = 'mobile.brand'
    brand_name = fields.Char(string="Mobile Brand", required=True)
  #  brand=fields.One2many('product.phone','product_id',string='product')


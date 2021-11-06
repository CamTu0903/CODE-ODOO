
from datetime import datetime, date, timedelta
from odoo import models, fields, api, _
from odoo.exceptions import Warning, UserError
import pytz
class MobileBrand(models.Model):
    _name = 'mobile.brand'
    _rec_name = 'brand_name'

    brand_name = fields.Char(string="Mobile Brand", required=True)


class MobileBrandModels(models.Model):
    _name = 'brand.model'
    _rec_name = 'mobile_brand_models'

    mobile_brand_name = fields.Many2one('mobile.brand', string="Mobile Brand", required=True)
    mobile_brand_models = fields.Char(string="Model Name", required=True)
    image_medium = fields.Binary(string='image', store=True, attachment=True)

class ThoiLuongBH(models.Model):
    _name = 'warranty.model'
    _rec_name = 'warranty_model'

    warranty_model = fields.Char(string="Warranty period", required=True)

class QuaTangKem(models.Model):
    _name = 'bundled.gift'
    _rec_name = 'bundled_gift'

    bundled_gift = fields.Char(string="Bundled gift", required=True)

class ChiNhanh(models.Model):
    _name = 'branch.model'
    _rec_name = 'branch_model'

    branch_model = fields.Char(string="Branch", required=True)

class DoiTuongKH(models.Model):
    _name = 'customer.model'
    _rec_name = 'customer_object'

    customer_object = fields.Char(string="Customer object", required=True)

class Color(models.Model):
    _name = 'color.model'
    _rec_name = 'color_model'

    color_model = fields.Char(string="Colour", required=True)

#returns
class GuiQua(models.Model):
    _name = 'sent.through'
    _rec_name = 'sent_through'

    sent_through = fields.Char(string="Sent through", required=True)
    mota=fields.Text('Description')





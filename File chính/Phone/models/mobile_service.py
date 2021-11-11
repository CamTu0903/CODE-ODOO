
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
    mota=fields.Text(string='Descriptions')

class QuaTangKem(models.Model):
    _name = 'bundled.gift'
    _rec_name = 'bundled_gift'

    bundled_gift = fields.Char(string="Bundled gift", required=True)
    image_medium=fields.Binary (String='Image')
    MoTa = fields.Text(string='Descriptions')

class ChiNhanh(models.Model):
    _name = 'branch.model'
    _rec_name = 'branch_model'

    branch_model = fields.Char(string="Branch", required=True)
    address_details=fields.Text(string='Address details')

class DoiTuongKH(models.Model):
    _name = 'customer.model'
    _rec_name = 'customer_object'

    customer_object = fields.Char(string="Customer object", required=True)

class Color(models.Model):
    _name = 'color.model'
    _rec_name = 'color_model'

    color_model = fields.Char(string="Colour", required=True)

class Pin(models.Model):
    _name = 'pin.model'
    _rec_name = 'pin_model'

    pin_model = fields.Char(string="Colour", required=True)

class NCC(models.Model):
    _name = 'ncc.model'
    _rec_name = 'ncc_model'

    maNCC = fields.Char(string='SupplierID', required=True, copy=False, readonly=True,
                            default=lambda seft: _('New'))
    image = fields.Binary(String='Image')
    ncc_model=fields.Char(string='Supplier',required=True)
    Sdt = fields.Char('Phone number')
    DC = fields.Text('Address')
    Email = fields.Char(string='Email')
    status = fields.Selection([
        ('stop providing', 'Stop providing'),
        ('continue to provide', 'Continue to provide'),
    ], string='Status')

    @api.model
    def create(self, vals):
        if vals.get('maNCC', ('New')) == ('New'):
            vals['maNCC'] = self.env['ir.sequence'].next_by_code('ncc.model') or _('New')
        res = super(NCC, self).create(vals)
        return res

#returns
class GuiQua(models.Model):
    _name = 'sent.through'
    _rec_name = 'sent_through'

    maVC = fields.Char(string='TransportersID', required=True, copy=False, readonly=True,
                        default=lambda seft: _('New'))
    sent_through = fields.Char(string="Sent through", required=True)
    Hotline=fields.Char('Support Hotline')
    image = fields.Binary(String='Image')
    DC = fields.Text('Address')
    DichVu=fields.Boolean('Express delivery',default=False)
    ThuTien=fields.Boolean('Collect money',default=False)
    TimeLV=fields.Text(string='Working time')

    @api.model
    def create(self, vals):
        if vals.get('maVC', ('New')) == ('New'):
            vals['maVC'] = self.env['ir.sequence'].next_by_code('sent.through') or _('New')
        res = super(GuiQua, self).create(vals)
        return res




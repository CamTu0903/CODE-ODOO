from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

# import models


class ProductPhone(models.Model):
    _name = "product.phone"
    _inherits = {'product.template': 'product_phone_id'}
    _description = "Product Phone"

    name = fields.Char('New Name', required=True)
    owner_id = fields.Many2one('res.partner', string='Owner')

    product_phone_id = fields.Many2one(
        'product.template', 'Phone',
        auto_join=True, index=True, ondelete="cascade", required=True)

    MoTaSP = fields.Text('Description')

    SoLuong = fields.Integer('Number')

    TinhTrang = fields.Selection([
        ('stocking', 'Stocking'),
        ('out of stock', 'Out Of Stock'),
    ], string='Status', default='stocking')
    BaoHanh = fields.Boolean('Warranty', default=False)
    #
    TLBH = fields.Float(digits=(1, 36), help="Duration in months")
    #
    Qua = fields.Many2one('product.category', string='Quà tặng kèm') # tạo model
    TinhTrangMua = fields.Selection([
        ('buy now', 'Buy now'),
        ('installment purchase', 'Installment purchase'),
    ], string='Purchase status', default='buy now')
    #

    TonKho = fields.Integer('Inventory')
    ThuMua = fields.Boolean('Repurchase', default=False)
    DoiTuongKH = fields.Selection([
        ('student', 'Student'),
        ('worker', 'Worker'),
        ('technology fanatics', 'Technology Fanatics'),
    ], string='Customer object', default='student')

    Suppliers = fields.Many2one('res.company', string='Nhà cung cấp')

    bonus_price = fields.Float("Bonus Price", default=0)
    basic_price = fields.Float("Basic Price", default=0)
    final_price = fields.Float("Final Price", compute='_compute_final_price')

    def _compute_final_price(self):
        for record in self:
            record.final_price = record.basic_price + record.bonus_price

    product_ids = fields.Many2many('product.product', string='Related Products')

class MobileBrandModels(models.Model):
    _name = 'brand.model'
    _rec_name = 'mobile_brand_models'

    mobile_brand_name = fields.Many2one('mobile.brand', string="Mobile Brand", required=True)
    mobile_brand_models = fields.Char(string="Model Name", required=True)
    image_medium = fields.Binary(string='image', store=True, attachment=True)

class MobileGiftModels(models.Model):
    _name = 'gift.mobile'
    _rec_name = 'mobile_gift_models'

    mobile_gift_name = fields.Many2one('gift.mobile', string="Gift", required=True)
    mobile_gift_models = fields.Char(string="Model", required=True)

class MobilePKModels(models.Model):
    _name = 'pk.mobile'
    _rec_name = 'mobile_pk_models'

    mobile_pk_name = fields.Many2one('pk.mobile', string="Phụ kiện", required=True)
    mobile_pk_models = fields.Char(string="Model", required=True)







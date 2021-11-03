from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class ProductPhone(models.Model):
    _name = "product.phone"
    _description = "Product Phone"

    product_id = fields.Char(string='PhoneID', required=True, copy=False, readonly=True,
                       default=lambda seft: _('New'))
    name = fields.Char('New Name', required=True)
    owner_id = fields.Many2one('res.partner', string='Owner')

    # product_phone_id = fields.Many2one(
    #     'product.template', 'Phone',
    #     auto_join=True, index=True, ondelete="cascade", required=True,default=lambda seft: _('New'))

    MoTaSP=fields.Text('Description')
    #quanhe many2one tao object cho nhanhieu
    NhanHieu=fields.Selection([
        ('samsung', 'SAMSUNG'),
        ('oppo', 'OPPO'),
        ('vivo', 'VIVO'),
        ('apple', 'APPLE'),
        ('xiaomi','XIAOMI')
    ], string='Brand', default='samsung')
    SoLuong=fields.Integer('Number')
    TinhTrang=fields.Selection([
        ('stocking', 'Stocking'),
        ('out of stock', 'Out Of Stock'),
    ], string='Status', default='stocking')
    BaoHanh=fields.Boolean('Warranty',default=False)
    #
    ThoiLGBH=fields.Float(digits=(1, 36), help="Duration in months")
    #
    TinhTrangMua=fields.Selection([
        ('buy now', 'Buy now'),
        ('nstallment purchase', 'Installment purchase'),
    ], string='Purchase status', default='buy now')
    #
    TonKho=fields.Integer('Inventory')
    ThuMua=fields.Boolean('Repurchase',default=False)

    PhuKien=fields.Selection([
        ('phone case', 'Phone case'),
        ('earphone', 'Earphone'),
        ('backup charger', 'Backup charger'),
        ('tempered glass', 'Tempered glass'),
        ('memory card support', 'Memory card support'),
        ('phone cleaning tools', 'Phone cleaning tools'),
        ('bluetooth', 'Bluetooth'),
    ], string='Accessory', default='phone case')

    bonus_price = fields.Float("Bonus Price", default=0)
    basic_price = fields.Float("Basic Price", default=0)
    final_price = fields.Float("Final Price", compute='_compute_final_price')

    #
    Qua_Tang = fields.One2many('product.gift', 'gift', string='Gift', required=True)
    NCC = fields.One2many('product.suppliers', 'suppliers', string='Suppliers', required=True)
    Doituong_KH = fields.One2many('product.customers', 'customers', string='Potential customers', required=True)
    Chi_nhanh = fields.One2many('product.branch', 'branch', string='Branch', required=True)

    def _compute_final_price(self):
        for record in self:
            record.final_price = record.basic_price + record.bonus_price

    product_ids = fields.Many2many('product.product', string='Related Products')

class gift(models.Model):
    _name = "product.gift"
    _description = "gift model"

    gift = fields.Many2one('product.phone', string='Gift')

class Suppliers(models.Model):
    _name = "product.suppliers"
    _description = "suppliers model"

    suppliers = fields.Many2one('product.phone', string='Suppliers')

class customers(models.Model):
    _name = "product.customers"
    _description = "customers model"

    customers = fields.Many2one('product.phone', string='Potential customers')

class branch(models.Model):
    _name = "product.branch"
    _description = "branch model"

    branch = fields.Many2one('product.phone', string='Branch')

    @api.model
    def create(self, vals):
        if vals.get('product_id', ('New')) == ('New'):
            vals['product_id'] = self.env['ir.sequence'].next_by_code('product.phone') or _('New')
        res = super(ProductPhone, self).create(vals)
        return res
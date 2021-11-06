
from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.template'

    is_a_parts = fields.Boolean(
        'Is a Mobile Part', default=False,
        help="Specify if the product is a mobile part or not.")

    brand_name = fields.Many2one('mobile.brand', String="Brand", help="Select a mobile brand for the part")
    model_name = fields.Many2one('brand.model', String="Model Name", domain="[('mobile_brand_name','=',brand_name)]",
                                 help="Select a model for the part")
    color_model = fields.Many2one('color.model',string="Colour", help="colour for the part")
    extra_descriptions = fields.Text(string="Note")

    SoLuong = fields.Integer('Number')
    TinhTrang = fields.Selection([
        ('stocking', 'Stocking'),
        ('out of stock', 'Out Of Stock'),
    ], string='Status', default='stocking')
    BaoHanh = fields.Boolean('Warranty', default=False)
    TinhTrangMua = fields.Selection([
        ('buy now', 'Buy now'),
        ('nstallment purchase', 'Installment purchase'),
    ], string='Purchase status', default='buy now')
    TonKho = fields.Integer('Inventory')
    sale_man = fields.Many2one('res.users', 'Saleperson')
    #
    ThoiLGBH = fields.Selection([
        ('6mth', '6 Month'),
        ('8mth', '8 Month'),
        ('12mth', '12 Month'),
    ], string='Warranty period', default='6mth')
    QuaTangKem = fields.Selection([
        ('earphone', 'Earphone'),
        ('phone case', 'Phone case'),
    ], string='Bundled gift', default='earphone')
    ChiNhanh = fields.Selection([
        ('tphcm', 'TPHCM'),
        ('ha noi', 'Ha Noi'),
        ('da nang', 'Da Nang'),
        ('ha tinh', 'Ha Tinh'),
        ('hai duong', 'Hai Duong'),
    ], string='Branch', default='tphcm')
    ThuMua = fields.Boolean('Repurchase', default=False)
    DoiTuongKH = fields.Selection([
        ('student', 'Student'),
        ('worker', 'Worker'),
        ('technology fanatics', 'Technology Fanatics'),
    ], string='Customer object', default='student')

    version=fields.Char('Software Version')
    ModelNumber=fields.Char(String='Model Number')
    Pin=fields.Char('Pin')

    TL_BH = fields.Many2one('warranty.model', string="Warranty period", required=True)
    bundled_gift = fields.Many2one('bundled.gift', string="Bundled gift", required=True)
    branch_model = fields.Many2one('branch.model', string="Branch", required=True)
    customer_object = fields.Many2one('customer.model', string="Customer object", required=True)
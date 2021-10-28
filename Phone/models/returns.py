# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class ReturnsGoods(models.Model):
    _name = "returns.goods"
    _description = "Returns goods model"
    name = fields.Char('Goods Name', required=True)
    madonhang = fields.Char(string='Mã Đơn Hàng', required=True, copy=False, readonly=True,
                       default=lambda seft: _('New'))
    SoLuong=fields.Integer('Number')
    TinhTrangHangHoa=fields.Text('Condition of goods')

  #  Phone_image = fields.Binary(string="Image", help="Image")
    Phone_image = fields.Binary(
        string="Image",
        required=True
    )

    LyDoTraHang=fields.Text('Return reason')
    Request=fields.Selection([
        ('change', 'Change'),
        ('return', 'Return'),
    ], string='Request', default='change')
    Method=fields.Selection([
        ('return the warehouse', 'Return the warehouse'),
        ('return the provider', 'Return the provider'),
        ('change device ownership', 'Change device ownership'),
    ], string='Method', default='return the warehouse')
    NgayTao=fields.Date('Date', required=False)
    ChiuThue=fields.Boolean('Tax',default=False)
    Status = fields.Selection([
        ('exchange','Exchange'),
        ('repair', 'Repair'),
        ('don"t use', 'Don"t Use'),
        ('upgrade', 'Upgrade'),
    ], string='Status', default='exchange')
    owner_id = fields.Many2one('res.partner', string='Owner')
    HoanTien=fields.Boolean('Refund',default=False)
    GuiQua=fields.Selection([
        ('viettel post', 'Viettel Post'),
        ('vnpost', 'VNpost'),
        ('giao hàng nhanh (GHN)', 'Giao Hàng Nhanh (GHN)'),
        ('giao hàng tiết kiệm (GHTK)','Giao Hàng Tiết Kiệm (GHTK)'),
        ('kerry express','Kerry Express'),
        ('shipchung','Shipchung')
    ], string='Sent through', default='viettel post')
    GhiChu=fields.Text('Notes')
    DonVi=fields.Char('Unit', default='Chiec')
    HotLine=fields.Char(string='Hotline', default='1800 1060')
    Phone_image = fields.Binary("Phone Image", attachment=True, help="Phone Image")


    @api.model
    def create(self, vals):
        if vals.get('madonhang', ('New')) == ('New'):
            vals['madonhang'] = self.env['ir.sequence'].next_by_code('returns.goods') or _('New')
        res = super(ReturnsGoods, self).create(vals)
        return res

# -*- coding: utf-8 -*-

from odoo import _,models, fields, api


class doitra(models.Model):
    _name = 'doitra.manage'
    _description = 'doitra.doitra'

    name = fields.Char(string='Mã Đơn Hàng', required=True, copy=False, readonly=True,
                       default=lambda seft: _('New'))
    soluong = fields.Integer(string="Sỗ lượng")
    tingtrang = fields.Selection([('connguyen', 'Còn Nguyên'), ('huhong', 'Đã Hư Hỏng')],
                                 string='Tình Trạng', default='connguyen')
    lido=fields.Text(string='Lý do trả hàng ')
    yeucau=fields.Selection([('doi', 'Đổi'), ('tra', 'Trả')],
                                 string='Yêu Cầu', default='doi')
    hinhthuc=fields.Selection([('tralaikho', 'Trả Lại Kho '), ('ncc', 'Nhà CUng Cấp'),('thaydoi','Thay đổi quyền sở hữu thiết bị')],
                                 string='Hình Thức', default='tralaikho')
    ngaytao=fields.Date(string='Ngày Tạo')
    chiuthue=fields.Boolean(string='Chịu thuế')
    trangthai=fields.Selection([('traodoi', 'Trao Đổi'), ('sua', 'Sửa'),('khongdungnua','Không dùng nữa'),('nagcap','Nâng Cấp')],
                                 string='Trạng thái', default='')
    ghichu=fields.Text(string='Ghi chú')
    xacnhan=fields.Selection([('yes', 'Yes'), ('no', 'No')],
                                 string='Xác Nhận', default='yes')
    donvi=fields.Selection([('', ''), ('', '')],
                                 string='Đơn Vị', default='')
    owner=fields.Text(string='Owner')
    hotline=fields.Text(string='Hotline')
    trongluong=fields.Float(string='Trọng Lượng')
    guiqua=fields.Selection([('buudien', 'Bưu Điện'), ('ghtk', 'Giao Hàng Tiết Kiệm'),('khac','Khác')],
                                 string='Gửi Qua', default='')



    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('doitra.manage') or _('New')
        res = super(doitra, self).create(vals)
        return res

#     value2 = fields.Float(compute="_value_pcy", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

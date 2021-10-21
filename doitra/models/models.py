# -*- coding: utf-8 -*-

from odoo import models, fields, api


class doitra(models.Model):
    _name = 'doitra.manage'
    _description = 'doitra.doitra'

    madonhang = fields.Integer(string="Mã đơn hàng")
    soluong = fields.Integer(string="Sỗ lượng")
    tingtrang = fields.Selection([('connguyen', 'Còn Nguyên'), ('huhong', 'Đã Hư Hỏng')],
                                 string='Trạng thái', default='')
    lido=fields.Text(string='Lý do trả hàng ')
    yeucau=fields.Selection([('doi', 'Đổi'), ('tra', 'Trả')],
                                 string='Trạng thái', default='doi')
    hinhthuc=fields.Selection([('tralaikho', 'Trả Lại Kho '), ('ncc', 'Nhà CUng Cấp'),('thaydoi','Thay đổi quyền sở hữu thiết bị')],
                                 string='Hình Thức', default='doi')
    ngaytao=fields.Date(string='Ngày Tạo')
    chiuthue=fields.Boolean(string='Chịu thuế')
    trangthai=fields.Selection([('traodoi', 'Trao Đổi'), ('sua', 'Sửa'),('khongdungnua','Không dùng nữa'),('nagcap','Nâng Cấp')],
                                 string='Trạng thái', default='')
    ghichu=fields.Text(string='Ghi chú')
    xacnhan=fields.Selection([('yes', 'Yes'), ('no', 'No')],
                                 string='Trạng thái', default='Yes')
    donvi=fields.Selection([('', ''), ('', '')],
                                 string='Đơn Vị', default='')
    owner=fields.Text(string='Owner')
    hotline=fields.Text(string='Hotline')
    trongluong=fields.Float(string='Trọng Lượng')




#     value2 = fields.Float(compute="_value_pcy", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

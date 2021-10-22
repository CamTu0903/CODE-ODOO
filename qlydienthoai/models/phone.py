from odoo import models, fields, api

class phone(models.Model):
    _name = "phone.phone"
    _description = "My Phone"

    MaSP = fields.Char ("Mã sản phẩm")
    Ten = fields.Char("Tên sản phẩm")
    MoTa = fields.Text()
    LoaiSP = fields.Selection([('moi','Mới'), ('cu','Cũ')], string='Loại sản phẩm')
    NhanHieu = fields.Selection([('samsung', 'Samsung'), ('apple', 'Apple')], string='Nhãn hiệu')
    BaoHanh = fields.Boolean("Có bảo hành", default=False)
    ThoiLuongBH = fields.Selection([('6th', '6 tháng'),
                                    ('8th', '8 tháng'),
                                    ('12th', '12 tháng')], string='Thời lượng bảo hành')
    SL = fields.Integer(string = 'Số lượng')
    TinhTrang = fields.Selection([('con', 'còn'), ('het', 'hết')], string='Tình trạng')
    GiaNhap = fields.Float("Giá nhập", compute='_nhap')
    GiaBan = fields.Float("Giá bán", compute='_ban')
    Qua = fields.Selection([('case', 'Case'), ('cuong luc', 'Cường lực')], string='Quà')
    TinhTrangMua = fields.Selection([('muangay', 'Mua ngay'), ('tragop', 'Trả Góp')],
                                     string='Tình trạng mua')
    ChiNhanh = fields.Selection([('hcm', 'HCM'),
                                 ('dn', 'DN'),
                                 ('hn', 'HN')], string='Chi nhánh')
    TonKho = fields.Integer(string = 'Số lượng')
    TrongLuong = fields.Char("Trọng lượng")
    NhaCungCap = fields.Char("Nhà cung cấp")
    DoiTuong = fields.Char("Nhà cung cấp")
    ThuMua = fields.Boolean("Thu mua lại", default=False)





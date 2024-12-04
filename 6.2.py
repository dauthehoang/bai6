print("ĐẬU THẾ HOÀNG")
print("MSSV:235752021610017")
class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

hinh_chunhat_1 = Hinhchunhat(7, 8)

dien_tich = hinh_chunhat_1.tinh_dien_tich()
print("Diện tích hình chữ nhật là:", dien_tich)

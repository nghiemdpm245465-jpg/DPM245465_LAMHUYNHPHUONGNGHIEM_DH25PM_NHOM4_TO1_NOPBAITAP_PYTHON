#Câu 7: Tối ưu chuỗi danh từ 

def ToiUuChuoiDanhTu(s):
    
    s = s.strip()
    tu = s.split()
    tu = [t.capitalize() for t in tu]
    s_toi_uu = " ".join(tu)
    
    return s_toi_uu


chuoi = input("Nhập chuỗi : ")

chuoi_toi_uu = ToiUuChuoiDanhTu(chuoi)
print("Chuỗi tối ưu:", chuoi_toi_uu)
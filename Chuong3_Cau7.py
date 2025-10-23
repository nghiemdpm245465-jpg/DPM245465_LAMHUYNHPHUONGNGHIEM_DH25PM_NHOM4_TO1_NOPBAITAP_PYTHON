#Câu 7: Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày vừa nhập (ngày/tháng/năm).

def nam_nhuan(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhap nam: "))
sntt = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if thang == 2 and nam_nhuan(nam):
    sntt[2] = 29
ngay += 1
if ngay > sntt[thang]:
    ngay = 1
    thang += 1
    if thang > 12:
        thang = 1
        nam += 1
print("Ngay ke tiep la: ", ngay, "/", thang, "/", nam)
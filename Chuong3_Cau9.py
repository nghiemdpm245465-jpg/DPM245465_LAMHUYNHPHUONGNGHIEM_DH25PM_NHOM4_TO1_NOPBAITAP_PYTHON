#Câu 9: Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm.

thang=int(input("Nhap thang: "))
if thang in (1,2,3):
    print("Quy 1")
elif thang in (4,5,6):
    print("Quy 2")
elif thang in (7,8,9):
    print("Quy 3")
elif thang in (10,11,12):
    print("Quy 4")
else:
    print("Khong hop le !")
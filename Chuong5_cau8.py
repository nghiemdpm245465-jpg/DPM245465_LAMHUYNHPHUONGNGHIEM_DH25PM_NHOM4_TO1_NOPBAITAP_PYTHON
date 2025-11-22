#Câu 8: Tách lấy tên bài hát 

def LayTenFile(duong_dan):

    vi_tri_sau_cung = max(duong_dan.rfind('/'), duong_dan.rfind('\\'))
    ten_file = duong_dan[vi_tri_sau_cung + 1:]
    return ten_file

def LayTenBaiHat(duong_dan):
    
    ten_file = LayTenFile(duong_dan)
    vi_tri_cham = ten_file.rfind('.')
    
    if vi_tri_cham != -1:
        ten_bai_hat = ten_file[:vi_tri_cham]
    else:
        ten_bai_hat = ten_file  
    return ten_bai_hat


duong_dan = input("Nhập đường dẫn file nhạc: ")

ten_file = LayTenFile(duong_dan)
ten_bai_hat = LayTenBaiHat(duong_dan)

print("Tên file đầy đủ:", ten_file)
print("Tên bài hát:", ten_bai_hat)
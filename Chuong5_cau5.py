#Câu 5: Xử lý chuỗi với các hàm cơ bản

chuoi = input("Nhập vào một chuỗi: ")


so_in_hoa = 0
so_in_thuong = 0
so_chu_so = 0
so_ky_tu_dac_biet = 0
so_khoang_trang = 0
so_nguyen_am = 0


nguyen_am = "aeiouAEIOU"


for c in chuoi:
    if c.isupper():          
        so_in_hoa += 1
    elif c.islower():        
        so_in_thuong += 1
    if c.isdigit():          
        so_chu_so += 1
    if c.isspace():          
        so_khoang_trang += 1
    if c in nguyen_am:       
        so_nguyen_am += 1
    if not c.isalnum() and not c.isspace():  
        so_ky_tu_dac_biet += 1


print("Số chữ IN HOA:", so_in_hoa)
print("Số chữ in thường:", so_in_thuong)
print("Số chữ là chữ số:", so_chu_so)
print("Số chữ là ký tự đặc biệt:", so_ky_tu_dac_biet)
print("Số chữ là khoảng trắng:", so_khoang_trang)
print("Số chữ là Nguyên Âm:", so_nguyen_am)
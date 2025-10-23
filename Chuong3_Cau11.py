#Câu 11: Kiểm tra số nguyên tố

while True:
    n=int(input("Nhập n: "))
    dem=0
    for i in range(1, n+1):
        if n%i == 0:
            dem += 1
    if dem == 2:
        print(n, "la so nguyen to")
    elif dem != 2:
        print(n, "khong phai so nguyen to")
    hoi=input("Ban co muon tiep tuc chuong trinh khong? (Y/N): ")
    if hoi in ("Y", "y"):
        continue
    else:
        print("")
        break
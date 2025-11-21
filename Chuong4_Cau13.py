def tong_uoc(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

# Hàm kiểm tra số hoàn thiện
def la_so_hoan_thien(n):
    return tong_uoc(n) == n

# Hàm kiểm tra số thịnh vượng
def la_so_thinh_vuong(n):
    return tong_uoc(n) > n

# Nhập số từ bàn phím
n = int(input("Nhập số nguyên dương n: "))

if n <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    if la_so_hoan_thien(n):
        print(f"{n} là số hoàn thiện.")
    else:
        print(f"{n} không phải là số hoàn thiện.")

    if la_so_thinh_vuong(n):
        print(f"{n} là số thịnh vượng.")
    else:
        print(f"{n} không phải là số thịnh vượng.")
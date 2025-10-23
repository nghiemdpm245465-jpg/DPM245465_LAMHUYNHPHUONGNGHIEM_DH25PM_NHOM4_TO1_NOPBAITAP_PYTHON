#Trả lời câu hỏi số 18 chương 3
def hinh_vuong_rong(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
def hinh_tam_giac(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j == 1 or i == n or i == j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
##Hình 3 đang bị lỗi, chưa fix được
"""def hinh_3(n):
    if n <= 0:
        return
    for i in range(n, 0, -1):
        print(" " * (n - i), end="")
        print("*", end="")
        if i > 1:
            print(" " * (2 * i - 3), end="")
            print("*", end="")
        print()
    for i in range(2, n + 1):
        print(" " * (n - i), end="")
        print("*", end="")
        if i > 1:
            print(" " * (2 * i - 3), end="")
            print("*", end="")
        print()
    print("\n")
"""
n = int(input("Nhap chieu cao n: "))
print("Hinh 1: ")
hinh_vuong_rong(n)

print("\nHinh 2: ")
hinh_tam_giac(n)

print("\nHinh 3 : ")
hinh_3(n)
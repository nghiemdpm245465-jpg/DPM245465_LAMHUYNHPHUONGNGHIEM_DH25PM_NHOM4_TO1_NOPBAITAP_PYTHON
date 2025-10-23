#Câu 18: Vẽ các hình dưới đây

def hinh_vuong_rong(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()  # xuống dòng sau mỗi hàng
n = int(input("Nhập chiều cao hình vuông: "))
hinh_vuong_rong(n)

def tam_giac_vuong(n):
    for i in range(1, n + 1):
        print('* ' * i)
n = int(input("Nhập chiều cao tam giác: "))
tam_giac_vuong(n)

def hinh_chu_L(n):
    for i in range(n):
        for j in range(n):
            if i == n - 1 or j == 0:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print() 
n = int(input("Nhập chiều cao hình chữ L: "))
hinh_chu_L(n)
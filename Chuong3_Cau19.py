#Trả lời câu hỏi số 19 chương 3
import math
print("Chương trình tính giá trị biểu thức S")
x = float(input("Nhap X: "))
n = float(input("Nhap n: "))
if x <= 0 or n <= 0 or n != int(n):
    print("X va n phai lon hon 0!")
else:
    S = 0
    for i in range(int(n)+1):
        S += x ** (2 * i + 1) / math.factorial(2 * i + 1)
    print("Gia tri bieu thuc S la: ", S)
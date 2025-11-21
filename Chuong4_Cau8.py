#Câu 8: Viết chương trình tính loga x 

import math

a = float(input("Nhập a: "))
x = float(input("Nhập x: "))

if a > 0 and a != 1 and x > 0:
    log_ax = math.log(x) / math.log(a)
    print("log_{}({}) = {}".format(a, x, log_ax))
else:
    print("Giá trị không hợp lệ! Cần: a > 0, a != 1, x > 0.")
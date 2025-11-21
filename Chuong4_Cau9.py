#Câu 9: Viết chương trình tính căn bậc 2 lồng nhau

import math

n = int(input("Nhập n: "))

s = 0
for i in range(n):
    s = math.sqrt(2 + s)

print("S(n) =", s)
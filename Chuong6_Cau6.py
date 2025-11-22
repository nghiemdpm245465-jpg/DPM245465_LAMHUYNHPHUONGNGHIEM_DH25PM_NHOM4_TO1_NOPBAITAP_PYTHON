#Câu 6: Nhập vào 1 list có N số ngẫu nhiên KHÔNG TRÙNG NHAU

import random

N = int(input("Nhập N: "))
lst = []

while len(lst) < N:
    x = random.randint(0, 100)
    if x not in lst:
        lst.append(x)

print("List ngẫu nhiên không trùng nhau:", lst)
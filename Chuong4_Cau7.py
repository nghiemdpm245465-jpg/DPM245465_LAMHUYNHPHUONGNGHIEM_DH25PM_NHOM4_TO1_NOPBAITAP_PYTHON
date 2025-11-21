#Câu 7: Tính và xuất độ dài đoạn AB 

import math


xA = float(input("Nhap xA: "))
yA = float(input("Nhap yA: "))
xB = float(input("Nhap xB: "))
yB = float(input("Nhap yB: "))

dAB = math.sqrt((xB - xA)**2 + (yB - yA)**2)

print("Độ dài đoạn AB:", dAB)

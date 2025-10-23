#Câu 8: Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Hãy xuất kết quả theo đúng phép toán đã nhập.

a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
pt=["+","-","*","/"]
pt=(input("Nhap phep tinh: "))
if pt == "+":
    print(a,"+",b)
elif pt == "-":
    print(a,"-",b)
elif pt == "*":
    print(a,"*",b)
elif pt == "/":
    if b!=0:
        print(a,"/",b)
    else:
        print("Khong the chia cho 0")
else:
    print("Phep tinh khong hop le!")
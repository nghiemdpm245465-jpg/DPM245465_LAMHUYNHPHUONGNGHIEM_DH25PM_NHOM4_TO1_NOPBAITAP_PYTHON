#Câu 19: Tính giá trị biểu thức S

def S(x, n):
    s = 0.0
    t = x      
    s += t
    for k in range(1, n + 1):
        t = t * (x * x) / (2 * k * (2 * k + 1))
        s += t
    return s
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

kq = S(x, n)
print("Giá trị S({}, {}) = {:.10f}".format(x, n, kq))
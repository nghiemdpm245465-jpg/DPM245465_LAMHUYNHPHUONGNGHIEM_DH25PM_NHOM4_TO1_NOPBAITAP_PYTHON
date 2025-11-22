#Câu 10: Xử lý Ma Trận 

def nhap_matrix(name):
    r = int(input(f"Nhập số dòng của {name}: "))
    c = int(input(f"Nhập số cột của {name}: "))

    print(f"Nhập các phần tử của {name}:")
    M = []
    for i in range(r):
        row = []
        for j in range(c):
            x = float(input(f"{name}[{i}][{j}] = "))
            row.append(x)
        M.append(row)
    return M

def cong_matrix(A, B):
    r = len(A)
    c = len(A[0])
    C = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C

def transpose(M):
    r = len(M)
    c = len(M[0])
    T = []
    for j in range(c):
        row = []
        for i in range(r):
            row.append(M[i][j])
        T.append(row)
    return T

A = nhap_matrix("A")
B = nhap_matrix("B")

print("A + B =")
for row in cong_matrix(A, B):
    print(row)

print("Transpose(A) =")
for row in transpose(A):
    print(row)

print("Transpose(B) =")
for row in transpose(B):
    print(row)
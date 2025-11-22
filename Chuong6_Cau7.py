#Câu 7: Viết chương trình nhập vào một dãy các số theo thứ tự tăng, nếu nhập sai quy cách thì yêu cầu nhập lại. In dãy số sau khi đã nhập xong 

n = int(input("Nhập số lượng phần tử: "))

lst = []

for i in range(n):
    while True:
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        if i == 0 or x > lst[-1]:     
            lst.append(x)
            break
        else:
            print("Sai quy tắc! Phải nhập số lớn hơn số trước đó. Nhập lại!")

print("Dãy số đã nhập:", lst)
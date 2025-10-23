#Câu 16: Cho biết bao nhiêu dấu * được in ra trên màn hình

count = 0
for a in range(20, 100, 5):
    print('*', end='')
    count += 1
print()  # xuống dòng
print("Số dấu * được in là:", count)
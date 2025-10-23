#Câu 14: Cho biết bao nhiêu dấu * được in ra trên màn hình

a = 0
while a <= 100:
    b = 0
    while b <= 40:
        if (a + b) % 2 == 0:
            print('*', end='')
        b += 1
    print()
    a += 1

    ###### Có 2071 dấu * được in ra cho 101 dòng và 41 cột #####
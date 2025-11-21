#Câu 12: Hàm oscillate

def oscillate(start, end):

    for i in range(3, 0, -1):
        yield -i
        yield i
        

    yield 0
    yield 0
    
   
    for i in range(1, 5): 
        yield i
        yield -i
        
for n in oscillate(-3, 5):
    print(n, end=' ')
print()    
#Câu 6: Trích lọc số âm trong chuỗi 

import re  

def NegativeNumberInStrings(s):
  

    so_am = re.findall(r'-\d+', s)
    
 
    so_am = [int(num) for num in so_am]
    
    return so_am

chuoi = input("Nhập chuỗi: ")
ketqua = NegativeNumberInStrings(chuoi)
print("Các số âm là:", ketqua)
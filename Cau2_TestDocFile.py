from Cau2_XulyFile import DocFileSo 

file_path = "csdl_so.txt"


arrSo = DocFileSo(file_path)

if arrSo is not None:
    print("\n--- a) Xuất list số từ mỗi dòng ---")
    

    for i, num_list in enumerate(arrSo, 1):
        
        print(f"Dòng {i}: {num_list}")

        so_am_list = [num for num in num_list if num < 0]
        
        if so_am_list:
            print(f"   => Số âm: {so_am_list}")
        else:
            print("   => Số âm: Không có")
    
    print("-----------------------------------")
def DocFileSo(path):
    """
    Hàm đọc tệp số, chuyển đổi mỗi dòng thành danh sách các số thực (float).
    """
    arrSo = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip()
                
                str_list = data.split(',')
                
                try:
                    num_list = [float(s) for s in str_list if s]
                    arrSo.append(num_list)
                except ValueError:
                    
                    print(f"Lỗi chuyển đổi kiểu dữ liệu ở dòng: {data}. Dòng này bị bỏ qua.")
                    arrSo.append([]) 
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy tệp {path}.")
        return None
    return arrSo
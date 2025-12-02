#Câu 9: Phần mềm tính BMI 

import tkinter as tk
from tkinter import messagebox

def tinh_bmi(height, weight):
    """Tính toán chỉ số BMI."""
   
    try:
        if height <= 0 or weight <= 0:
            return None, "Chiều cao và cân nặng phải lớn hơn 0"
        
       
        if height >= 10:
            height_m = height / 100
        else:
            height_m = height
            
        bmi = weight / (height_m ** 2)
        return bmi, None
    except TypeError:
        return None, "Lỗi kiểu dữ liệu"
    except ZeroDivisionError:
        return None, "Chiều cao không thể bằng 0"

def phan_loai_bmi(bmi):
    """Phân loại tình trạng cân nặng dựa trên BMI."""
 
    if bmi < 18.5:
        tinh_trang = "Gầy"
        nguy_co = "Thấp"
    elif 18.5 <= bmi < 25.0:
        tinh_trang = "Bình thường"
        nguy_co = "Trung bình"
    elif 25.0 <= bmi < 30.0:
        tinh_trang = "Mập"
        nguy_co = "Cao"
    else: 
        tinh_trang = "Béo phì"
        nguy_co = "Rất cao"
        
    return tinh_trang, nguy_co

def xu_ly_tinh_bmi():
    """Hàm xử lý khi nhấn nút 'Tính BMI'."""
    try:

        chieu_cao = float(entry_chieu_cao.get())
        can_nang = float(entry_can_nang.get())
        
        bmi_value, error = tinh_bmi(chieu_cao, can_nang)
        
        if error:
            messagebox.showerror("Lỗi", error)
            return

        tinh_trang, nguy_co = phan_loai_bmi(bmi_value)
        
     
        label_bmi_result.config(text=f"{bmi_value:.2f}")
        label_tinh_trang_result.config(text=tinh_trang)
        label_nguy_co_result.config(text=nguy_co)
        
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ cho Chiều cao và Cân nặng.")

def thoat_chuong_trinh():
    """Hàm xử lý khi nhấn nút 'Thoát'."""
    root.quit()
    root.destroy()




root = tk.Tk()
root.title("Phần mềm tính BMI")


frame_main = tk.Frame(root, bg="yellow", padx=20, pady=20, borderwidth=2, relief="solid")
frame_main.grid(row=0, column=0, padx=10, pady=10)


frame_main.grid_columnconfigure(1, weight=1)
frame_main.grid_columnconfigure(2, weight=1)


tk.Label(frame_main, text="Nhập chiều cao:", bg="yellow").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_chieu_cao = tk.Entry(frame_main, width=15, justify='center')
entry_chieu_cao.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="ew")
entry_chieu_cao.insert(0, "1.8")


tk.Label(frame_main, text="Nhập cân nặng:", bg="yellow").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_can_nang = tk.Entry(frame_main, width=15, justify='center')
entry_can_nang.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky="ew")
entry_can_nang.insert(0, "72") # Giá trị mặc định (kg)


btn_tinh_bmi = tk.Button(frame_main, text="Tính BMI", command=xu_ly_tinh_bmi, bg="#87CEEB") # Màu xanh nhạt
btn_tinh_bmi.grid(row=2, column=1, columnspan=2, padx=5, pady=10, sticky="ew")




tk.Label(frame_main, text="BMI của bạn:", bg="yellow").grid(row=3, column=0, padx=5, pady=5, sticky="w")
label_bmi_result = tk.Label(frame_main, text="X", bg="white", relief="solid", width=15)
label_bmi_result.grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky="ew")


tk.Label(frame_main, text="Tình trạng của bạn:", bg="yellow").grid(row=4, column=0, padx=5, pady=5, sticky="w")
label_tinh_trang_result = tk.Label(frame_main, text="Hơi Béo", bg="white", relief="solid", width=15)
label_tinh_trang_result.grid(row=4, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

tk.Label(frame_main, text="Nguy cơ phát triển bệnh:", bg="yellow").grid(row=5, column=0, padx=5, pady=5, sticky="w")
label_nguy_co_result = tk.Label(frame_main, text="Hơi hơi cao", bg="white", relief="solid", width=15)
label_nguy_co_result.grid(row=5, column=1, columnspan=2, padx=5, pady=5, sticky="ew")


btn_thoat = tk.Button(frame_main, text="Thoát", command=thoat_chuong_trinh, bg="red", fg="white")
btn_thoat.grid(row=6, column=1, columnspan=2, padx=5, pady=10, sticky="ew")

root.mainloop()
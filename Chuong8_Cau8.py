#Câu 8: Thiết kế màn hình chuyển độ F thành độ C 

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def chuyen_doi_f_sang_c():
    try:
        do_f = float(entry_f.get())
        
        do_c = (do_f - 32) * 5 / 9
        
        ket_qua = f"{do_c:.2f}"
        
        label_c_result.config(text=ket_qua)
        
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số hợp lệ cho độ F.")
        label_c_result.config(text="Lỗi")

root = tk.Tk()
root.title("Chuyển đổi Độ F sang Độ C")

frame_main = tk.Frame(root, bg="yellow", padx=20, pady=20, borderwidth=2, relief="solid")
frame_main.grid(row=0, column=0, padx=10, pady=10)

tk.Label(frame_main, text="Nhập độ F", bg="yellow").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_f = tk.Entry(frame_main, width=10, justify='center')
entry_f.grid(row=0, column=2, padx=5, pady=5)
entry_f.insert(0, "350")

btn_chuyen = tk.Button(frame_main, text="Chuyển", bg="blue", command=chuyen_doi_f_sang_c)
btn_chuyen.grid(row=1, column=2, padx=5, pady=5)

tk.Label(frame_main, text="Độ C", bg="yellow").grid(row=2, column=0, padx=5, pady=5, sticky="w")
label_c_result = tk.Label(frame_main, text="Độ C ở đây", bg="yellow", width=10, relief="solid")
label_c_result.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

root.mainloop()
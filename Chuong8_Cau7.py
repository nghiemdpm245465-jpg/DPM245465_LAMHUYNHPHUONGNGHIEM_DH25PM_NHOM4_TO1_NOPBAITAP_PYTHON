#Câu 7: Thiết kế màn hình chuyển năm Dương Lịch thành Âm Lịchimport tkinter as tk

import tkinter as tk

def chuyen():
    try:
        year = int(entry.get())
        
        can = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
        chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

        can_index = (year + 6) % 10    
        chi_index = (year + 8) % 12    

        result.set(can[can_index] + " " + chi[chi_index])
    except:
        result.set("Lỗi!")

root = tk.Tk()
root.title("Chuyển năm Dương → Âm")

tk.Label(root, text="Nhập năm dương:", bg="yellow").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root, width=10)
entry.grid(row=0, column=1)

tk.Button(root, text="Chuyển", bg="blue", command=chuyen, width=10).grid(row=0, column=2, padx=10)

tk.Label(root, text="Năm âm:", bg="yellow").grid(row=1, column=0)
result = tk.StringVar()
tk.Label(root, textvariable=result, fg="yellow").grid(row=1, column=1)

root.mainloop()
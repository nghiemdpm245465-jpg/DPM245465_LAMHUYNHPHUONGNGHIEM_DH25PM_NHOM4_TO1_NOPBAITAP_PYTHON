#Câu 6: Màn hình cấu hình Style cho Button 

import tkinter as tk

root = tk.Tk()
root.title("frame2")

reliefs = ["raised", "sunken", "flat", "ridge", "groove", "solid"]

row = 0
for bd in range(0, 5):
    tk.Label(root, text=f"borderwidth = {bd}").grid(row=row, column=0, padx=5)

    col = 1
    for rf in reliefs:
        tk.Button(root, text=rf, relief=rf, borderwidth=bd, width=7).grid(row=row, column=col, padx=2, pady=2)
        col += 1

    row += 1

root.mainloop()
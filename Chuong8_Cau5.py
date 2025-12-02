#Câu 5: Màn hình đăng nhập

import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Enter New Password")
root.geometry("300x180")

correct_old_pass = "123"  

def change_password():
    old = old_pass.get()
    new = new_pass.get()
    re = re_pass.get()

    if old != correct_old_pass:
        messagebox.showerror("Error", "Old password incorrect!")
        return
    if new == "" or re == "":
        messagebox.showerror("Error", "Password cannot be empty!")
        return
    if new != re:
        messagebox.showerror("Error", "New passwords do not match!")
        return

    messagebox.showinfo("Success", "Password changed successfully!")

tk.Label(root, text="Old Password:").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="New Password:").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Enter New Password Again:").grid(row=2, column=0, padx=10, pady=5)

old_pass = tk.Entry(root, show="*")
new_pass = tk.Entry(root, show="*")
re_pass = tk.Entry(root, show="*")

old_pass.grid(row=0, column=1)
new_pass.grid(row=1, column=1)
re_pass.grid(row=2, column=1)

tk.Button(root, text="OK", width=10, command=change_password).grid(row=3, column=0, pady=10)
tk.Button(root, text="Cancel", width=10, command=root.destroy).grid(row=3, column=1)

root.mainloop()
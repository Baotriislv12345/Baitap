import customtkinter as ctk
from math import *
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app=ctk.CTk()
app.geometry("450x270")
app.iconbitmap("D:\\tài liệu word\\dhv.ico")
app.title("giải phương trình bậc 2")
title=ctk.CTkLabel(app,text="giải phương trình bậc 2",font=("Arial",18,"bold"))
title.grid(row=0,column=0,columnspan=3,pady=15)
entry_a=ctk.CTkEntry(app,placeholder_text="nhập a",width=150)
entry_a.grid(row=1,column=0,pady=10)
entry_b=ctk.CTkEntry(app,placeholder_text="nhập b",width=150)
entry_b.grid(row=1,column=1,pady=10)
entry_c=ctk.CTkEntry(app,placeholder_text="nhập c",width=150)
entry_c.grid(row=1,column=2,pady=10)
result=ctk.CTkLabel(app,text="",font=("Arial",14))
result.grid(row=3,column=0,columnspan=3,pady=10)
def tinh():
    try:
        a=float(entry_a.get())
        b=float(entry_b.get())
        c=float(entry_c.get())
        delta=b**2-4*a*c
        if delta<0:
            result.configure(text="phương trình vô nghiệm")
        elif delta==0:
            x=-b/(2*a)
            result.configure(text=f"phương trình có nghiệm kép x={x}")
        else:
            x1=(-b+sqrt(delta))/(2*a)
            x2=(-b-sqrt(delta))/(2*a)
            result.configure(text=f"phương trình có 2 nghiệm phân biệt \nx1={x1}\nx2={x2}")
    except:
        result.configure(text="lỗi nhập liệu")
app.button=ctk.CTkButton(app,text="tính",command=tinh)
app.button.grid(row=2,column=1,pady=10)

app.mainloop()
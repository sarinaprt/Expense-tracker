from tkinter import *
from tkinter import ttk
import webbrowser as link
import matplotlib.pyplot as plt
# ایجاد کردن صفحه
window = Tk()
title = window.title("Expense Tracker")
window.geometry("450x600")
window.resizable(False, False)
window.config(bg="#F9FAFB")

# بالای صفحه_بودجه
BudgetBox = Entry(window, bg="#C3D8E6", font=("Arial", 30), bd=2, fg="white", justify="center")
BudgetBox.place(width=450, height=230)

# کلید شارژ
add_Button = Button(window, text="+", bg="#D8EAF2", font=40, bd=2)
add_Button.place(width=40, height=40, x=390, y=280)
add_label = Label(window, text="شارژ حساب", bg="#D8EAF2", font=50, bd=2)
add_label.place(width=160, height=40, x=230, y=280)

# کلید کسر
reduce_button = Button(window, text="-", bg="#D8EAF2", font=40, bd=2)
reduce_button.place(width=40, height=40, x=390, y=340)
reduce_label = Label(window, text="کسر از حساب", bg="#D8EAF2", font=50, bd=2)
reduce_label.place(width=160, height=40, x=230, y=340)

# متن خدمات دیگر
label = Label(window, text="......خدمات دیگر", justify="right", anchor=E, width=35, font=10, fg="#8B9688")
label.place(y=380)

# بخش برای پایین
canv=Canvas(window,bg="#FFFFFF",height=180,width=420)
canv.pack(side=BOTTOM)


# قاب دکمه‌ها داخل Canvas
fram_chose = Frame(canv, background="#D5E5ED", height=180, width=430)
canv.create_window((0, 0), window=fram_chose, anchor="nw")

def new_page(text):

    def Focus_in(event):
        remind_entry.delete(0,END)
    def focus_out(event):
        if remind_entry.get()=="":  
            remind_entry.insert(0,"متن مورد نظر را وارد کنید")

 
    def add_to_checkbutton():
        get_entry = remind_entry.get()
        if get_entry and get_entry != "متن مورد نظر را وارد کنید":
            Checkbutton(check_fram, text=f"{get_entry}", bg="#D8EAF2").pack(side="top",)
            remind_entry.delete(0, END)  




    second_page=Toplevel(window)
    second_page.title(f"{text}")
    second_page.geometry("450x600")
    label=Label(second_page,text=f"{text}",font=("B Nazanin",14)).pack(side="top")
    if text==" حساب":
        columns=("data","action","plus/minus")
        trees=ttk.Treeview(second_page,columns=columns)
        for col in columns:
            trees.column(col,width=100)
        trees.heading("data",text="تاریخ")
        trees.heading("action",text="عملیات")
        trees.heading("plus/minus",text="بودجه")
        s=trees.insert("",END,values=("2000/02/03","buy","-100"))
        trees.insert(s,END,text="تاریخ اون روز",values=("12:30","buy","-100"))
        trees.pack(pady=50)
    elif text=="یادآور":
        remind_entry=Entry(second_page,font=("B Nazanin",12),bg="#C3D8E6",fg="#898C8C",width=30)
        remind_entry.insert(0,"متن مورد نظر را وارد کنید")
        remind_entry.bind("<FocusIn>", Focus_in)
        remind_entry.bind("<FocusOut>", focus_out)
        remind_entry.place(x=50, y=50)
        button_remind_entry=Button(second_page,text="apply",bg="#8EBCBD",width=4,command=add_to_checkbutton)
        button_remind_entry.place(x=50, y=80)
        check_fram=Frame(second_page,bg="#ABD4E0")
        check_fram.place(x=50, y=110)
    elif text=="پشتیبان‌گیری":
        Label(second_page,text="درصورت وجود مشکل میتوانید با همکاران ما ارتباط بگیرید ",font=("B Nazanin",14),bg="#8EBCBD").pack(side="top",padx=10,pady=20)
        Label(second_page,text="098*********",font=12).pack(side="top")
        LINK_TEL=Label(second_page,text="ارتباط با پشتیبان تلگرام",font=("Arial", 12, "underline"),cursor="hand2")
        LINK_TEL.pack(side="top")
        LINK_TEL.bind("<Button-1>",lambda e: open_lin() )

        def open_lin():
            link.open("https://t.me/YourTelegramID")
    elif text=="جزییات و نمودار":
        fram_char=Frame(second_page,bg="#FFFFFF",height=300).pack(side="top",fill="x")
        plt.pie([25,30,45],labels=["A","B","C"],autopct="%1.1f%%")
        plt.show()






# لیست دکمه‌ها
boton = [
    ("تنظیمات", "⚙️", 1, 0), ("حساب", "💳", 1, 1), ("جزییات و نمودار", "📈", 1, 2),
    ("یادآور", "⏰", 2, 0), ("پشتیبان‌گیری", "💾", 2, 1),  ("پروفایل", "👤", 2, 2)]

def buttons_shap(master,text,icon):
    buttons=Button(master,text=f"{text}\n {icon}",font=("B Nazanin",12),
                   width=12,height=5,relief=RAISED,justify="center",command=lambda t=text: new_page(t))
    return buttons
#کلید 
for (text,icon,row,column) in boton:
    bt=buttons_shap(fram_chose,text,icon)
    bt.grid(row=row,column=column,padx=5,pady=5)


#اسکرول بار
scroll=Scrollbar(window,orient="vertical",command=canv.yview)
scroll.pack(fill=Y,side="right")
canv.configure(yscrollcommand=scroll.set)  

def on_configure(event):
    canv.configure(scrollregion=canv.bbox("all"))

fram_chose.bind("<Configure>", on_configure)


  
window.mainloop()




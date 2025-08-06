from tkinter import *

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
    second_page=Toplevel(window)
    second_page.title(f"{text}")
    second_page.geometry("450x600")
    label=Label(second_page,text=f"{text}",font=("B Nazanin",14)).pack(side="top",)



# لیست دکمه‌ها
boton = [
    ("جزییات حساب", "💳", 1, 0), ("جزییات حساب", "💳", 1, 1), ("جزییات حساب", "💳", 1, 2),
    ("یادآور", "⏰", 2, 0), ("پشتیبان‌گیری", "💾", 2, 1), ("نظرات", "📩", 2, 2),
    # برای تست اسکرول بیشتر اضافه کن:
    ("تنظیمات", "⚙️", 3, 0), ("راهنما", "📘", 3, 1), ("تماس با ما", "☎️", 3, 2),
    ("پروفایل", "👤", 4, 0), ("خروج", "🚪", 4, 1), ("درباره ما", "ℹ️", 4, 2)
]
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




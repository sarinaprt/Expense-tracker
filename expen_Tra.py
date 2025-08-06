from tkinter import *

# ایجاد کردن صفحه
window = Tk()
title = window.title("Expense Tracker")
window.geometry("450x600")
window.resizable(False, False)
window.config(bg="#F9FAFB")

# بالای صفحه_بودجه
BudgetBox = Entry(window, bg="#b2ccc4", font=("Arial", 30), bd=2, fg="white", justify="center")
BudgetBox.place(width=450, height=230)

# کلید شارژ
add_Button = Button(window, text="+", bg="#7cb4af", font=40, bd=2)
add_Button.place(width=40, height=40, x=410, y=280)
add_label = Label(window, text="شارژ حساب", bg="#7cb4af", font=50, bd=2)
add_label.pack(width=160, height=40, x=250, y=280)

# کلید کسر
reduce_button = Button(window, text="-", bg="#7cb4af", font=40, bd=2)
reduce_button.place(width=40, height=40, x=410, y=340)
reduce_label = Label(window, text="کسر از حساب", bg="#7cb4af", font=50, bd=2)
reduce_label.place(width=160, height=40, x=250, y=340)

# متن خدمات دیگر
label = Label(window, text="......خدمات دیگر", justify="right", anchor=E, width=40, font=10, fg="#8B9688")
label.place(y=380)

# بخش برای پایین
canv = Canvas(window, background="#694B46", height=180)
canv.pack(fill="x", side=BOTTOM)

# ایجاد اسکرول‌بار
s = Scrollbar(window, orient="vertical", command=canv.yview)
s.pack(side=RIGHT, fill=Y)

canv.configure(yscrollcommand=s.set)

# قاب دکمه‌ها داخل Canvas
fram_chose = Frame(canv, background="#403D3D", height=180, width=430)
window_id = canv.create_window((0, 0), window=fram_chose, anchor="nw")

# تابع به‌روزرسانی ناحیه اسکرول
def on_configure(event):
    canv.configure(scrollregion=canv.bbox("all"))

fram_chose.bind("<Configure>", on_configure)

# تابع دکمه‌ها
def button_inf(master, text, icon):
    buttons = Button(master, text=f"{icon}\n{text}", wraplength=100, font=("B Nazanin", 12),
                     width=12, height=5, relief=RAISED, justify="center")
    return buttons

# لیست دکمه‌ها
boton = [
    ("جزییات حساب", "💳", 1, 0), ("جزییات حساب", "💳", 1, 1), ("جزییات حساب", "💳", 1, 2),
    ("یادآور", "⏰", 2, 0), ("پشتیبان‌گیری", "💾", 2, 1), ("نظرات", "📩", 2, 2),
    # برای تست اسکرول بیشتر اضافه کن:
    ("تنظیمات", "⚙️", 3, 0), ("راهنما", "📘", 3, 1), ("تماس با ما", "☎️", 3, 2),
    ("پروفایل", "👤", 4, 0), ("خروج", "🚪", 4, 1), ("درباره ما", "ℹ️", 4, 2)
]

# چیدمان دکمه‌ها
for (text, icon, row, column) in boton:
    bt = button_inf(fram_chose, text, icon)
    bt.grid(row=row, column=column, padx=5, pady=5)

window.mainloop()

from tkinter import *
from tkinter import ttk
menu = {
    "Pizza": 40.00,
    "Tacos": 49.00,
    "Sandwich": 30.00,
    "Burger": 32.00,
    "Frites": 15.00,
    "Nuggets": 35.00,
    "Soda": 15.00,
    "Limonade": 18.00
}
menuu = Tk()
menuu.title("Food Menu")
menuu.geometry("390x500")
menuu.config(bg="#acf2e4")
menuu.minsize(390,500)
menuu.maxsize(390,500)
menuu.resizable(0,0)

quantities = {item: IntVar(value=0) for item in menu}
total_price = DoubleVar(value=0.0)

def update_total():
    total = sum(menu[item] * quantities[item].get() for item in menu)
    total_price.set(total)

def decrease_quantity(item):
    if quantities[item].get() > 0:
        quantities[item].set(quantities[item].get() - 1)
        update_total()

Label(menuu, text="Food Menu", font=("Verdana", 18, "bold"),bg="#acf2e4").pack(pady=10)

menu_frame = Frame(menuu)
menu_frame.pack(pady=10)

for item, price in menu.items():
    item_frame = Frame(menu_frame)
    item_frame.pack(fill=X, pady=5)

    Label(item_frame, text=f"{item} - {price:.2f} DH", font=("Fixedsys", 14),bg="#acf2e4").pack(side=LEFT, padx=10)

    quantity_label = Label(item_frame, textvariable=quantities[item], width=3, font=("Arial", 14), bg="#acf2e4")
    quantity_label.pack(side=RIGHT, padx=10)

    Button(item_frame, text="+",bg="#7fcc6a",width=3,
           command=lambda i=item: (quantities[i].set(quantities[i].get() + 1),  update_total())).pack(side=RIGHT)
    Button(item_frame, text="-",width=3, bg= "#d67676",command=lambda i=item: decrease_quantity(i)).pack(side=RIGHT)

Label(menuu, text="Total:", font=("Arial", 16),bg= "#acf2e4").pack(pady=10)
total_label = Label(menuu, textvariable=total_price, font=("Arial", 16),bg="#acf2e4")
total_label.pack(pady=10)

def update_total_label():
    total = total_price.get()
    total_label.config(text=f"{total:.2f} DH")

total_price.trace("w", lambda *args: update_total_label())

menuu.mainloop()
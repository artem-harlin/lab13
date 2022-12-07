from tkinter import *
from tkinter import ttk

def click():
    print("На данный момент скидок нет")
    
root = Tk()
root.title("AUTO SERVICE")
root.geometry("250x200")

btn = ttk.Button(text = "Cкидки", command = click)
btn.pack(anchor="nw")
btn = ttk.Button(text = "Автомобили")
btn.pack(anchor="nw")
btn = ttk.Button(text = "Марка")
btn.pack(anchor="nw")
btn = ttk.Button(text = "Список сотрудников")
btn.pack(anchor="nw")


root.mainloop()




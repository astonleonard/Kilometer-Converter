from tkinter import *


def convert():
    miles = float(Miles_number.get())
    km = round(miles * 1.609)
    Km_result.config(text=f'{km}')


window = Tk()
window.config(padx=20, pady=20)

Miles_number = Entry()
Miles_number.grid(column=1, row=0)
Miles_number.config(width=7)

Miles_label = Label(text='Miles')
Miles_label.grid(column=2, row=0)
Miles_label.config(padx=10)

is_equal_to = Label(text='is equal to')
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=10)

Km_result = Label(text='0')
Km_result.grid(column=1, row=1)
Km_result.config(padx=10)

Km_Label = Label(text='Km')
Km_Label.grid(column=2, row=1)
Km_Label.config(padx=10)

Calculate = Button(text='Calculate', command=convert)
Calculate.grid(column=1, row=3)
Calculate.config(padx=10)

window.mainloop()

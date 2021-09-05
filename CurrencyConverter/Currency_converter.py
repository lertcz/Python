import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

url = 'https://api.exchangerate-api.com/v4/latest/USD'

data = requests.get(url).json()
currencies = data['rates']

NAMES = []

for x in currencies:
    NAMES.append(x)

#print(NAMES)

def convert(from_cur, to_cur, amount):
    if(from_cur != to_cur):
        amount = amount / currencies[from_cur]
        
    amount = round(amount * currencies[to_cur], 4)
    return amount


#print(convert('USD','CZK',1))


gui = tk.Tk()

gui.title("Currency converter")        
gui.geometry("600x350")

#init drop box values --
var1 = StringVar(gui)
var1.set(NAMES[0]) # default value

var2 = StringVar(gui)
var2.set(NAMES[0]) # default value

#create master frame ---
master_frame = Frame(gui)
master_frame.pack(pady=20)

#title -----------------
titleFrame = Frame(master_frame)

title = Label(titleFrame, text="Currency converter")
title.config(font=("Courier", 36))
title.pack()

convert_frame = Frame(master_frame)
convert_frame.grid(column=0, row=1)

#from ------------------
Frame1 = Frame(convert_frame)
Frame1.grid(column=0, row=0, padx=40, pady=30)

From = Label(Frame1, text="From:")

FromD = OptionMenu(Frame1, var1, *NAMES)

FromT = Entry(Frame1, width=25, justify='center')

From.grid(column=0, row=0)
FromD.grid(column=0, row=1)
FromT.grid(column=0, row=2)

#to --------------------
Frame2 = Frame(convert_frame)
Frame2.grid(column=1, row=0, padx=40, pady=30)

To = Label(Frame2, text="To:")

ToD = OptionMenu(Frame2, var2, *NAMES)

ToT = Entry(Frame2, width=25, justify='center')

To.grid(column=0, row=0)
ToD.grid(column=0, row=1)
ToT.grid(column=0, row=2)

#convert ----------------
def clicked():
    #print(var1.get(), FromT.get(), var2.get(), ToT.get())
    ToT.delete(0,"end")
    try:
        ToT.insert(0, convert(var1.get(), var2.get(), float(FromT.get())))

    except ValueError:
        pass

convertBtn = Button(master_frame, text="Convert", command=lambda:clicked())
convertBtn.config(font=("Courier", 10))

#title.grid(column=0, row=0)
titleFrame.grid(column=0, row=0)

#Frame1.grid(column=0, row=1)

#Frame2.grid(column=1, row=1)

convertBtn.grid(column=0, row=2, pady=50)

gui.mainloop()
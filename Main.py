#!/usr/bin/python
import tkinter
from tkinter import *
app = tkinter.Tk()
app.title("Please login")
# Code to add widgets will go here...
lblun = Label(app, text="Username", padx=125, pady=5)
lblun.grid(column=0, row=1)
txtun = Entry(app, width=10)
txtun.grid(column=1, row=2)
app.geometry('350x200')

app.mainloop()

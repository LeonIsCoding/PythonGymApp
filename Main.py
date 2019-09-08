#!/usr/bin/python
import tkinter
from tkinter import *
app = tkinter.Tk()
app.title("Please login")

# Code to add widgets will go here...
label1 = Label(app, text="Username").grid(sticky=E)
label2 = Label(app, text="Password").grid(sticky=E)
txtun = Entry(app, width=20)
txtun.grid(row=0, column=1)
txtpw = Entry(app, width=20, show="*")
txtpw.grid(row=1, column=1)


def authorizeuser():
    username = txtun.get()
    password = txtpw.get()


button1 = Button(app, text="Log in", command=authorizeuser).grid(row=2, column=2)

app.mainloop()

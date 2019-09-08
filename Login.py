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


def isuservalid():
    username = txtun.get().lower()
    password = txtpw.get().lower()
    if username and password == "admin":
        return True
    else:
        return False


def loginuser():
    from tkinter import messagebox
    if isuservalid():
        messagebox.showinfo("Success", "The user is valid")
    else:
        messagebox.showerror("Failure", "The user is NOT valid")


button1 = Button(app, text="Log in", command=loginuser).grid(row=2, column=2)

app.mainloop()

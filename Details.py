import tkinter
from tkinter import *
app = tkinter.Tk()
app.title("Enter customer details")

lblTitle = Label(app, text="Title").grid(sticky=E)
lblFirstName = Label(app, text="First name").grid(sticky=E)
lblSurname = Label(app, text="Surname").grid(sticky=E)
lblAddress = Label(app, text="First line of address").grid(sticky=E)
lblEmail = Label(app, text="Email address").grid(sticky=E)
lblNumber = Label(app, text="Phone number").grid(sticky=E)
lblExistingCustomer = Label(app, text="Is customer a gym member?").grid(sticky=E)
cbxExistingCustomer = Checkbutton(app).grid(column=1, row=6)

btnOk = Button(app, text="OK").grid(column=0, row=7)
btnExit = Button(app, text="Exit", command=app.destroy).grid(column=1, row=7)

app.mainloop()

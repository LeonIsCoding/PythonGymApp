import tkinter
from tkinter import *
app = tkinter.Tk()
app.title("Enter customer details")
app.geometry('300x190')
app.resizable(0, 0)

lblTitle = Label(app, text="Title").grid(sticky=E)
lblFirstName = Label(app, text="First name").grid(sticky=E)
lblSurname = Label(app, text="Surname").grid(sticky=E)
lblAddress = Label(app, text="First line of address").grid(sticky=E)
lblEmail = Label(app, text="Email address").grid(sticky=E)
lblNumber = Label(app, text="Phone number").grid(sticky=E)
lblExistingCustomer = Label(app, text="Is customer a gym member?").grid(sticky=E)
cbxExistingCustomer = Checkbutton(app).grid(column=1, row=6)
txtTitle = Entry(app, width=20)
txtTitle.grid(row=0, column=1)
txtFirstName = Entry(app, width=20)
txtFirstName.grid(row=1, column=1)
txtSurname = Entry(app, width=20)
txtSurname.grid(row=2, column=1)
txtAddress = Entry(app, width=20)
txtAddress.grid(row=3, column=1)
txtEmail = Entry(app, width=20)
txtEmail.grid(row=4, column=1)
txtNumber = Entry(app, width=20)
txtNumber.grid(row=5, column=1)

btnOk = Button(app, text="OK").grid(column=0, row=7)
btnExit = Button(app, text="Exit", command=app.destroy).grid(column=1, row=7)


def aredetailsvalid(title, fname, sname, address, email, number):
    if not title or fname or sname or address or email or number:
        return False
    else:
        return True


app.mainloop()

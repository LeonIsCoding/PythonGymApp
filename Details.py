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

btnExit = Button(app, text="Exit", command=app.destroy).grid(column=1, row=7)


def recorduser():
    from tkinter import messagebox
    if aredetailsvalid(txtTitle.get(), txtFirstName.get(), txtSurname.get(), txtAddress.get(), txtEmail.get(), txtNumber.get()):
        messagebox.showinfo("Success", "All details seem valid")
    else:
        messagebox.showerror("Failure", "Not all details are valid")


btnOk = Button(app, text="OK", command=recorduser).grid(column=0, row=7)


def aredetailsvalid(title, fname, sname, address, email, number):
    if not title or not fname or not sname or not address or not email or not number:
        return False
    else:
        createuser(title, fname, sname, address, email, number)
        return True


def createuser(title, fname, sname, address, email, number):
    UserDetails.set_Address(UserDetails(), address)
    UserDetails.set_Email(UserDetails(), email)
    UserDetails.set_FirstName(UserDetails(), fname)
    UserDetails.set_Number(UserDetails(), number)
    UserDetails.set_Surname(UserDetails(), sname)
    UserDetails.set_Title(UserDetails(), title)


app.mainloop()


class UserDetails:

    def __init__(self, Title=None, FirstName=None, Surname=None, Address=None, Email=None, Number=None):
        self.Title = Title
        self.FirstName = FirstName
        self.Surname = Surname
        self.Address = Address
        self.Email = Email
        self.Number = Number

    """ Constructors """

    def get_Title(self):
        return self.Title

    def set_Title(self, Title):
        self.Title = Title

    def get_FirstName(self):
        return self.FirstName

    def set_FirstName(self, FirstName):
        self.FirstName = FirstName

    def get_Surname(self):
        return self.Surname

    def set_Surname(self, Surname):
        self.Surname = Surname

    def get_Address(self):
        return self.Address

    def set_Address(self, Address):
        self.Address = Address

    def get_Email(self):
        return self.Email

    def set_Email(self, Email):
        self.Email = Email

    def get_Number(self):
        return self.Number

    def set_Number(self, Number):
        self.Number = Number
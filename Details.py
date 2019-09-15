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
varExistingCustomer = BooleanVar()
cbxExistingCustomer = Checkbutton(app, variable=varExistingCustomer).grid(column=1, row=6)
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


def record_user():
    from tkinter import messagebox
    if are_details_valid(txtTitle.get(), txtFirstName.get(), txtSurname.get(), txtAddress.get(), txtEmail.get(), txtNumber.get()):
        messagebox.showinfo("Success", "All details seem valid")
    else:
        messagebox.showerror("Failure", "Not all details are valid")


btnOk = Button(app, text="OK", command=record_user).grid(column=0, row=7)


def are_details_valid(title, first_name, surname, address, email, number):
    if not title or not first_name or not surname or not address or not email or not number:
        return False
    else:
        create_user(title, first_name, surname, address, email, number)
        return True


def create_user(title, first_name, surname, address, email, number):
    from Customer import Customer
    cu = Customer()
    cu.set_address(address)
    cu.set_email(email)
    cu.set_first_name(first_name)
    cu.set_number(number)
    cu.set_surname(surname)
    cu.set_title(title)
    cu.set_member(varExistingCustomer.get())


app.mainloop()

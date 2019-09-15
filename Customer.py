class Customer:

    def __init__(self, title=None, first_name=None, surname=None, address=None, email=None, number=None, member=None):
        self.title = title
        self.first_name = first_name
        self.surname = surname
        self.address = address
        self.email = email
        self.number = number
        self.member = member

    """ Constructors """

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.surname = surname

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def get_member(self):
        return self.member

    def set_member(self, member):
        self.member = member

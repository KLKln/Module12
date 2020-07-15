"""
Program: customer.py
Author: Kelly Klein
Last date modified: 7/13/2020
This program will create a class called customer allowing the user to
access information about a customer, also will raise AttributeError if
cid is not an int
"""


class InvalidCustomerIdException(Exception):
    pass


class InvalidNameException(Exception):
    pass


class InvalidPhoneNumberFormat(Exception):
    pass


class Customer:
    def __init__(self, customer_id, lname, fname, phone):
        """
use reST style.
    :param customer_id: int assigned to identify customer
    :param lname: customer's last name
    :param fname: customer's first name
    :param phone: customer's phone number
    :return:
"""
        try:
            while isinstance(customer_id, int) and 1000 <= customer_id <= 9999:
                self.cid = customer_id
                break
        except InvalidCustomerIdException:
            raise InvalidCustomerIdException("must be a whole number between 1000 and 9999")
        # customer_id: int: required
        try:
            while lname.isalpha():
                self.last_name = lname
                break
        except InvalidNameException:
            raise InvalidNameException("Alphabet characters only!")
        # last_name: string: required
        try:
            while fname.isalpha():
                self.first_name = fname
                break
        except InvalidNameException:
            raise InvalidNameException("Alphabet characters only!")
        try:
            for i, c in enumerate(phone):
                if i in [3, 7]:
                    if c != '-':
                        InvalidPhoneNumberFormat('phone format "xxx-xxx-xxxx" only')
                elif not c.isalnum():
                    InvalidPhoneNumberFormat('phone format "xxx-xxx-xxxx" only')
            self.phone = phone
        except InvalidPhoneNumberFormat('phone format "xxx-xxx-xxxx" only'):
            raise InvalidPhoneNumberFormat('phone format "xxx-xxx-xxxx" only')
        # phone_number: string: required

    def __str__(self):
        return str(self.cid) + ' ' + str(self.first_name) + ' ' + str(self.last_name) + ' ' + str(self.phone)

    def __repr__(self):
        return repr(str(self.cid) + self.first_name + self.last_name + self.phone)

    def display(self):
        # I tried adding try/catch to display hoping it would trigger 'raise' here but
        # I must be doing something wrong with my raise because it's not raising
        # an error, it just says:  "AttributeError: 'Customer' object has no attribute 'cid'"
        # this is obviously because my while statement isn't fulfilled, I just don't know
        # why
        try:
            print(str(self.cid))
        except InvalidCustomerIdException:
            raise InvalidCustomerIdException("must be a whole number between 1000 and 9999")
        try:
            print(str(self.first_name) + ' ' + str(self.last_name))
        except InvalidNameException:
            raise InvalidNameException("Alphabet characters only!")
        try:
            print(str(self.phone))
        except InvalidPhoneNumberFormat:
            raise InvalidPhoneNumberFormat('phone format "xxx-xxx-xxxx" only')


if __name__ == '__main__':
    gerta = Customer(1000, 'Haymaker', 'Gerta', '999-765-4321')
    gerta.display()
    hibby = Customer(999, 'Shibby', 'Hibby', '319-567-8900')
    hibby.display()
    pip = Customer(1000, '1000', 'Pip', 'phone')
    pip.display()

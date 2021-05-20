# Rodrigue Andela
# 05/19/2021
# in this task I first create a class employee that has private data then, I wrote a separate function that add dictionary

class Employee:

    __ID_number = 0
    __salary = 0
    __email_address = ''
    __Employee_name = ''

    def __init__(self, name, ID_number, salary, email_address):
        self.__name = name
        self.__ID = ID_number
        self.__salary = salary
        self.__email_address = email_address

    # Set the values of the data members of the class.

    def get_name(self):
        return self.__name

    def get_ID_number(self):
        return self.__ID_number

    def get_salary(self):
        return self.__salary

    def get_email_address(self):
        return self.__email_address

    # definite the function and add dictionary

def make_employee_dict(name, ID_number, salary, email_adress):
    Employees = dict()
    for i in range(len(name)):
        Employees[ID_number[i]] = Employee(name[i], ID_number[i], salary[i], email_adress[i])
    return Employees




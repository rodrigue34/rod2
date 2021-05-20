# Rodrigue Andela
# 05/19/2021
# in this task I first create a class employee that has private data then, I wrote a separate function that add dictionary

class Employee:
<<<<<<< HEAD

    __ID_number = 0
    __salary = 0
    __email_address = ''
    __Employee_name = ''

=======
>>>>>>> origin/main
    def __init__(self, name, ID_number, salary, email_address):
        self.__name = name
        self.__ID = ID_number
        self.__salary = salary
        self.__email_address = email_address

    # Set the values of the data members of the class.

    def get_name(self):
        return self.__name

    def get_ID_number(self):
        return self.__ID

    def get_salary(self):
        return self.__salary

    def get_email_address(self):
        return self.__email_address

    # definite the function and add dictionary

def make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails):
    employees = dict()
    for i in range(len(emp_names)):
        employees[emp_ids[i]] = Employee(emp_names[i], emp_ids[i], emp_sals[i], emp_emails[i])
    return employees


<<<<<<< HEAD
emp_names = ["Jean", "Kat", "Pomona"]
emp_ids = ["100", "101", "102"]
emp_sals = [30, 35, 28]
emp_emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
result = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)
print(result["100"].get_name())
=======

>>>>>>> origin/main



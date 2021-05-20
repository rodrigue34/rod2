# Rodrigue Andela
# 05/19/2021
# in this task I first create a class employee that has private data then, I wrote a separate function that add dictionary

class Employee:

    __ID_number = 0
    __email_address = ''
    __salary = 0
    __employee_name = ''

    def __init__(self, name, ID_number, salary, email_address):
        self.__name = name
        self.__ID = ID_number
        self.__salary = salary
        self.__email_address = email_address

        # definite the value data
    def get_name(self):
        return self.__name

    def get_ID_number(self):
        return self.__ID

    def get_salary(self):
        return self.__salary

    def get_email_address(self):
        return self.__email_address

# definition and dictionary
def make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails):
    employees = dict()
    for i in range(len(emp_names)):
        employees[emp_ids[i]] = Employee(emp_names[i], emp_ids[i], emp_sals[i], emp_emails[i])
    return employees







# Implement a class Company with private attributes __name, __revenue, and __employees. Provide public methods to set and get these attributes, ensuring that revenue is non-negative and employees are not empty.

class Company:
    def __init__(self):
        self.__name = ""
        self.__revenue = 0
        self.__employees = []

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_revenue(self, revenue):
        if revenue >= 0:
            self.__revenue = revenue
        else:
            print("Revenue cannot be negative.")

    def get_revenue(self):
        return self.__revenue

    def set_employees(self, employees):
        if employees:
            self.__employees = employees
        else:
            print("Employees list cannot be empty.")

    def get_employees(self):
        return self.__employees


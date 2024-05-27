# Create a class Bank with private attributes __name and __balance. Provide public methods to set the bank's name and get its balance.

class Bank:
    def __init__(self):
        self.__name = ""
        self.__balance = 0
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def get_balance(self):
        return self.__balance

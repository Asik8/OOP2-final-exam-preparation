# Implement a class House with private attributes __address, __num_rooms, and __price. Provide public methods to set and get these attributes, ensuring that the price cannot be negative.

class House:
    def __init__(self):
        self.__address = ""
        self.__num_rooms = 0
        self.__price = 0
    
    def set_address(self, address):
        self.__address = address
    
    def get_address(self):
        return self.__address
    
    def set_num_rooms(self, num_rooms):
        self.__num_rooms = num_rooms
    
    def get_num_rooms(self):
        return self.__num_rooms
    
    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Price cannot be negative")
    
    def get_price(self):
        return self.__price

# Create a class Household with private attributes __address, __num_rooms, and __occupants. Provide public methods to set and get these attributes, ensuring that the number of rooms is always a positive integer.

class Household:
    def __init__(self):
        self.__address = ""
        self.__num_rooms = 0
        self.__occupants = []
    
    def set_address(self, address):
        self.__address = address
    
    def get_address(self):
        return self.__address
    
    def set_num_rooms(self, num_rooms):
        if num_rooms > 0:
            self.__num_rooms = num_rooms
        else:
            print("Number of rooms must be positive")
    
    def get_num_rooms(self):
        return self.__num_rooms
    
    def set_occupants(self, occupants):
        self.__occupants = occupants
    
    def get_occupants(self):
        return self.__occupants

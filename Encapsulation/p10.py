# Implement a class Warehouse with private attributes __location, __capacity, and __items. Provide public methods to set and get these attributes, ensuring that capacity is a positive integer and items are not empty.

class Warehouse:
    def __init__(self):
        self.__location = ""
        self.__capacity = 0
        self.__items = []

    def set_location(self, location):
        self.__location = location

    def get_location(self):
        return self.__location

    def set_capacity(self, capacity):
        if capacity > 0:
            self.__capacity = capacity
        else:
            print("Capacity should be positive.")

    def get_capacity(self):
        return self.__capacity

    def set_items(self, items):
        if items:
            self.__items = items
        else:
            print("Items list cannot be empty.")

    def get_items(self):
        return self.__items

# Create a class Book with private attributes __title, __author, and __pages. Provide public methods to set and get these attributes, ensuring that the number of pages is always a positive integer.

class Book:
    def __init__(self):
        self.__title = ""
        self.__author = ""
        self.__pages = 0

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author

    def set_pages(self, pages):
        if pages > 0:
            self.__pages = pages
        else:
            print("Number of pages should be positive.")

    def get_pages(self):
        return self.__pages


class Book:
    def __init__(self, title, author, isbn, copies, pages=0):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_available = True
        self.__pages = pages
        self.copies = copies 
        self.is_available = True if copies > 0 else False
    
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_pages(self):
        return self.__pages
    
    def get_is_available(self):
        return self.__is_available
    
    def set_is_available(self, is_available):
        self.__is_available = is_available
    
    def get_isbn(self):
        return self.__isbn
    
    def issue_book(self):
        # if self.__is_available:
        #     self.__is_available = False
        #     return True
        # return False
        if self.is_available:
            self.copies -= 1
            if self.copies == 0:
                self.is_available = False
            else:
                print(f"The book {self.get_title()}, is not available. ")
    
    def return_book(self):
        # self.__is_available = True
        self.copies += 1
        self.is_available = True 
    
    def display_info(self):
        print(f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}, Available: {self.__is_available}")

class EBook(Book):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format
    
    # Mehtod Overriding
    def display_info(self):
        super().display_info()
        print(f"File Format: {self.file_format}")

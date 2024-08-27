
class Member:
    def __init__(self, name, membership_id, contact_info):
        self.__name = name
        self.__membership_id = membership_id
        self.__contact_info = contact_info
        self.issued_books = []
    
    @property
    def name(self):
        return self.__name
    
    @property
    def membership_id(self):
        return self.__membership_id
    
    @property
    def contact_info(self):
        return self.__contact_info
    
    def display_member_info(self):
        print(f"Member: {self.name}, Id: {self.membership_id}, Contact: {self.contact_info}")
    
    def issue_book(self, book):
        if book.is_available:
            book.issue_book()
            self.issued_books.append(book)
            print(f"Book: '{book.get_title()}' issued to {self.name}")
        else:
            print(f"Book: '{book.get_title()}' is not available")
    
    def return_book(self, book):
        if book in self.issued_books:
            book.return_book()
            self.issued_books.remove(book)
            print(f"Book: '{book.get_title()}' returned by {self.name}")
        else:
            print(f"Book: '{book.get_title()}' is not issued to {self.name}")


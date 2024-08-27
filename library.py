
from book import Book
from member import Member
from transaction import Transaction

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, title, author, isbn, pages=0):
        book = Book(title, author, isbn, pages)
        self.books.append(book)
    
    def add_member(self, name, membership_id, contact_info):
        member = Member(name, membership_id, contact_info)
        self.members.append(member)
    
    def find_book(self, isbn):
        for book in self.books:
            if book.get_isbn() == isbn:
                return book
        return None
    
    def find_member(self, membership_id):
        for member in self.members:
            if member.membership_id == membership_id:
                return member
        return None
    
    def issue_book(self, isbn, membership_id):
        book = self.find_book(isbn)
        member = self.find_member(membership_id)
        if book and member:
            transaction = Transaction(book, member)
            transaction.issue_book()
            return transaction
        return None
    
    def return_book(self, isbn, membership_id):
        book = self.find_book(isbn)
        member = self.find_member(membership_id)
        if book and member:
            transaction = Transaction(book, member)
            transaction.return_book()
            return transaction
        return None
    
    def display_books(self):
        for book in self.books:
            book.display_info()
    
    def display_members(self):
        for member in self.members:
            member.display_member_info()


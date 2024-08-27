
import unittest
from book import Book
from member import Member
from transaction import Transaction
from library import Library

""" book1 = Book("Python 101", "John Doe", "123456789")
print(f"Book: {book1.title}, Author: {book1.author}, Available: {book1.is_available}")
book1.issue_book()
print(f"Available after issue: {book1.is_available}")
book1.return_book()
print(f"Available after return: {book1.is_available}")

member1 = Member('Alice', "M123", "alice@gmail.com")
member1.display_member_info()
transaction1 = Transaction(book1, member1)
transaction1.issue_book()
transaction1.return_book()
 """
""" # Function to add a new book 
def add_book():
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")
    isbn = input("Enter Book ISBN: ")
    new_book = Book(title, author, isbn)
    return new_book

# Function to add a new member
def add_member():
    name = input("Enter Member Name: ")
    membership_id = input("Enter Membership Id: ")
    contact_info = input("Enter Contact Info: ")
    new_member = Member(name, membership_id, contact_info)
    return new_member

def main():
    # Example of adding a book and member, and issuing a book
    book1 = add_book()
    member1 = add_member()
    transaction1 = Transaction(book1, member1)
    transaction1.issue_book()
    transaction1.return_book()

main()
 """
def main():
    library = Library()
    
    # Adding books
    library.add_book("python 101", "John Doe", "123456789", 350)
    library.add_book("Lerning Django", "Jane Smith", "987654321", 450)
    
    # Adding members
    library.add_member("Alice", "M123", "alice@gmail.com")
    library.add_member("Bob", "M456", "bob@gmail.com")
    
    # Display books and members
    library.display_books()
    library.display_members()
    
    # Issuing a book 
    library.issue_book("123456789", "M123")
    
    # Returning a book 
    library.return_book("123456789", "M123")

# if __name__ == "__main__":
#     main()
main()
class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("Python 101", "John Doe", "123456789", 5, 350)
        
    def test_initial_availability(self):
        self.assertTrue(self.book.is_available)
    
    def test_issue_book(self):
        self.book.issue_book()
        self.assertEqual(self.book.copies, 4)
        self.book.issue_book()
        self.book.issue_book()
        self.book.issue_book()
        self.book.issue_book()
        self.assertFalse(self.book.is_available)
    
    def test_return_book(self):
        self.book.issue_book()
        self.book.return_book()
        self.assertEqual(self.book.copies, 5)
        self.assertTrue(self.book.is_available)
class TestMember(unittest.TestCase):
    def setUp(self):
        self.member = Member("Alice", "M123", "alice@gmail.com")
        self.book = Book("Python 101", "John Doe", "123456789", 5, 350)
        
    def test_issue_book(self):
        self.member.issue_book(self.book)
        self.assertIn(self.book, self.member.issued_books)
    
    def test_return_book(self):
        self.member.issue_book(self.book)
        self.member.return_book(self.book)
        self.assertNotIn(self.book, self.member.issued_books)

class TestTranssaction(unittest.TestCase):
    def setUp(self):
        self.book = Book("Python 101", "John Doe", "123456789", 5, 350)
        self.member = Member("Alice", "M123", "alice@gmail.com")
        self.transaction = Transaction(self.book, self.member)
    
    def test_issue_book(self):
        self.transaction.issue_book()
        self.assertIsNone(self.transaction.issue_date)
    
    def test_return_transaction(self):
        self.transaction.issue_book()
        self.transaction.return_book()
        self.assertIsNone(self.transaction.return_date)
    
    def test_transaction_history(self):
        self.transaction.issue_book()
        self.transaction.return_book()
        history = self.transaction.get_history()
        self.assertEqual(len(history), 1)

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.library.add_book("Python 101", "John Doe", "123456789", 350)
        self.library.add_member("Alice", "M123", "alice@gmail.com")
    
    def test_find_book(self):
        book = self.library.find_book("123456789")
        self.assertIsNotNone(book)
        self.assertEqual(book.get_title(), "Python 101")
    
    def test_find_member(self):
        member = self.library.find_member("M123")
        self.assertIsNotNone(member)
        self.assertEqual(member.name, "Alice")
    
    def test_issue_book(self):
        transaction = self.library.issue_book("123456789", "M123")
        self.assertIsNotNone(transaction)
        self.assertEqual(transaction.book.get_title(), "Python 101")
    
    def test_return_book(self):
        self.library.issue_book("123456789", "M123")
        transaction = self.library.return_book("123456789", "M123")
        self.assertIsNotNone(transaction)
        self.assertEqual(transaction.book.get_title(), "Python 101")

if __name__ == "__main__":
    unittest.main()
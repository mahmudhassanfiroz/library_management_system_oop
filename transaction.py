
from datetime import datetime

class Transaction:
    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.issue_date = None
        self.return_date = None
        self.__history = []
    
    
    def issue_book(self):
        if self.book.issue_book():
            self.issue_date = datetime.now()
            self.__history.append({
                "action": "issue",
                "date": self.issue_date,
                "book": self.book.get_title(),
                "member": self.member.name
            })
            print(f"Book: '{self.book.get_title()}' issued to {self.member.name} on {self.issue_date}")
        else:
            print(f"Book: '{self.book.get_title()}' is not availabel")
    
    def return_book(self):
        self.book.return_book()
        self.return_date = datetime.now()
        self.__history.append({
            "action": "return",
            "date": self.return_date,
            "book": self.book.get_title(),
            "member": self.member.name
        })
        print(f"Book: '{self.book.get_title()}' returned by {self.member.name} on {self.return_date}")

    def get_history(self):
        return self.__history


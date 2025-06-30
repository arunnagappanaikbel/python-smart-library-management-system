from core.models import Book
from core.utils import *
from core.admin import Admin
from core.member import MemberActions
import json

SETTINGS = {
    "books_file": "data/books.csv",
    "members_file": "data/members.json",
    "log_file": "data/logs.txt"
}

class Library:
    def __init__(self):
        self.books = load_books(SETTINGS['books_file'])
        self.members = load_members(SETTINGS['members_file'])
        setup_logger(SETTINGS['log_file'])

    def save_all(self):
        save_books(SETTINGS['books_file'], self.books)
        save_members(SETTINGS['members_file'], self.members)

if __name__ == "__main__":
    library = Library()
    admin = Admin(library)
    member_system = MemberActions(library)

    # Example actions
    admin.add_book(Book("101", "Data", "A1", 10))
    admin.add_book(Book("102", "RPA", "A2", 8))
    admin.add_book(Book("103", "QA", "A3", 5))
    admin.add_book(Book("104", "SPARK", "A4", 5))
    admin.add_book(Book("105", "PYTHON", "A5", 5))
    admin.add_book(Book("106", "SQL", "A6", 5))
    #library.members["m02"] = {"name": "Arun", "borrowed_books": set()}
    #borrow the book
    member_system.borrow_book("m01", "101")
    member_system.borrow_book("m01", "102")
    member_system.borrow_book("m01", "105")
    member_system.borrow_book("m01", "106")
    member_system.borrow_book("m02", "102")
    member_system.borrow_book("m02", "103")
    member_system.borrow_book("m02", "105")
    member_system.borrow_book("m02", "106")
    #Return the book
    member_system.return_book("m01", "102")
    member_system.return_book("m02", "103")

    library.save_all()
    
# ✅ Features Overview:
# 🧑‍💼 Admin Functions
# Add a new book

# Update existing book details

# Delete a book

# Search books by ID/title/author

# 👤 Member Functions
# Borrow a book (decreases book count)

# Return a book (increases book count)

# Check borrowed books

# ⚙️ System Features
# Use of:

# Lists: Store available books

# Dictionaries: Book/member records

# Tuples: For immutable book info

# Sets: Track unique borrowed book IDs

# Logging:

# Log every operation (borrow, return, errors) in logs.txt

# Error Handling:

# File not found, invalid input, unavailable book, etc.

# File Handling:

# Books: CSV

# Members: JSON

# Logs: Text

# Config Management:

# Load settings from settings.json

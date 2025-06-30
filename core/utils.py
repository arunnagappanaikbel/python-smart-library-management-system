import csv
import os
import logging, json
from core.models import Book

def load_books(file_path):
    books = {}
    if not os.path.exists(file_path):
        return books
    with open(file_path, mode = 'r', newline='') as f:
        reader = csv.DictReader(f)    
        for row in reader:
            books[row['book_id']] = Book(row['book_id'], row['title'], row['author'], row['copies'])    
    return books

def save_books(filepath, books):
    with open(filepath, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['book_id', 'title', 'author', 'copies'])
        writer.writeheader()
        for book in books.values():
            writer.writerow(vars(book))
            
def load_members(filepath):
    if os.path.exists(filepath):
        with open(filepath) as f:
            members = json.load(f)
            # Convert borrowed_books list back to set
            for m in members.values():
                m["borrowed_books"] = set(m["borrowed_books"])
            return members
    return {}

    
def save_members(filepath, members):
    # Convert sets to lists for JSON serialization
    serializable_members = {}
    for member_id, member_data in members.items():
        serializable_members[member_id] = {
            "name": member_data["name"],
            "borrowed_books": list(member_data["borrowed_books"])
        }
    with open(filepath, 'w') as f:
        json.dump(serializable_members, f, indent=2)

        

def setup_logger(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
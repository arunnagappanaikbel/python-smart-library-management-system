import logging
class Admin:
    def __init__(self, library):
        self.library = library
        
    def add_book(self, book):
        self.library.books[book.book_id] = book
        logging.info(f'Book added : {book.title}')
        
    def update_book(self, book_id, **kwargs):
        book = self.library.books.get(book_id)
        if not book:
            logging.error(f"Book ID {book_id} not found for update.")
            return False
        for key, value in kwargs.items():
            setattr(book, key, value)
        logging.info(f"Book updated: {book.title}")
        return True
    
        # if 'title' in kwargs:
        # book.title = kwargs['title'].strip()
        # if 'author' in kwargs:
        # book.author = kwargs['author'].strip()
        # if 'copies' in kwargs:
        # try:
        #     book.copies = int(kwargs['copies'])
        # except ValueError:
        #     print("[ERROR] Copies must be an integer.")
        #     return False

        logging.info(f"Book ID {book_id} updated successfully.")
        return True
                
    def delete_book(self, book_id):
        if book_id in self.library.books:
            del self.library.books[book_id]
            logging.info(f"Book deleted: {book_id}")
            return True
        logging.error(f"Book ID {book_id} not found for deletion.")
        return False

    def search_books(self, keyword):
        return [b for b in self.library.books.values() if keyword.lower() in b.title.lower()]
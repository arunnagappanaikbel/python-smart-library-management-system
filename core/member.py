import logging
class MemberActions:
    def __init__(self, library):
        self.library = library

    def borrow_book(self, member_id, book_id):
        member = self.library.members.get(member_id)
        book = self.library.books.get(book_id)
        if not member or not book:
            logging.error(f"Borrow failed. Member or Book not found.")
            return False
        if (book.copies) > 0:
            (book.copies) -= 1
            member['borrowed_books'].add(book_id)
            logging.info(f"Book borrowed: {book.title} by Member {member_id}")
            return True
        logging.error(f"No copies left for book {book_id}")
        return False

    def return_book(self, member_id, book_id):
        member = self.library.members.get(member_id)
        book = self.library.books.get(book_id)
        if not member or not book:
            logging.error(f"Return failed. Member or Book not found.")
            return False
        if book_id in member['borrowed_books']:
            book.copies += 1
            member['borrowed_books'].remove(book_id)
            logging.info(f"Book returned: {book.title} by Member {member_id}")
            return True
        logging.warning(f"Book {book_id} was not borrowed by Member {member_id}")
        return False
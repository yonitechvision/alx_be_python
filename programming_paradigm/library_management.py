class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self.__is_checked_out

class Library:
    def init(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def check_out_book(self, title):
        for book in self.__books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"Checked out: {title}"
        return f"Book '{title}' not available"

    def return_book(self, title):
        for book in self.__books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"Returned: {title}"
        return f"Book '{title}' was not checked out"

    def list_available_books(self):
        available_books = [book for book in self.__books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No available books")
from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    print("\n" + library.check_out_book("1984"))
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    print("\n" + library.return_book("1984"))
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()

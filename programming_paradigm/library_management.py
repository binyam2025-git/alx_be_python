# library_management.py

class Book:
    """Represents a book in the library."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False # Private attribute, initialized to False (available)

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out

class Library:
    """Manages a collection of books."""
    def __init__(self):
        self._books = [] # Private list to store Book instances

    def add_book(self, book_instance):
        """Adds a Book object to the library's collection."""
        if isinstance(book_instance, Book):
            self._books.append(book_instance)
        else:
            print("Can only add Book objects to the library.")

    def check_out_book(self, title):
        """
        Finds a book by title and checks it out if available.
        Prints a message indicating success or failure.
        """
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if book.is_available():
                    book.check_out()
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        if not found:
            print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """
        Finds a book by title and returns it if checked out.
        Prints a message indicating success or failure.
        """
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if not book.is_available():
                    book.return_book()
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' is already available.")
                return
        if not found:
            print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """Lists all books that are currently available."""
        available_found = False
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
                available_found = True
        if not available_found and not self._books:
             print("The library is empty.")
        elif not available_found:
             print("No books are currently available.")

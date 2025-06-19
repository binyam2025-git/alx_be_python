"""
library_system.py

This script defines classes for a library system, demonstrating
inheritance and composition in Python.

Classes:
    Book: A base class representing a generic book.
    EBook: A derived class for electronic books, inheriting from Book.
    PrintBook: A derived class for physical printed books, inheriting from Book.
    Library: A class managing a collection of Book, EBook, and PrintBook instances,
             demonstrating composition.
"""

class Book:
    """
    Base class for a generic book.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
    """
    def __init__(self, title: str, author: str):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Derived class for electronic books, inheriting from Book.

    Additional Attributes:
        file_size (int): The size of the e-book file in KB.
    """
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes a new EBook instance.

        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            file_size (int): The size of the e-book file in KB.
        """
        super().__init__(title, author) # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        """
        Returns a user-friendly string representation of the EBook,
        including its file size.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived class for physical printed books, inheriting from Book.

    Additional Attributes:
        page_count (int): The number of pages in the print book.
    """
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a new PrintBook instance.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the print book.
        """
        super().__init__(title, author) # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        """
        Returns a user-friendly string representation of the PrintBook,
        including its page count.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    Manages a collection of various book types (Book, EBook, PrintBook).
    Demonstrates composition by holding a list of book objects.

    Attributes:
        books (list): A list to store instances of Book, EBook, and PrintBook.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book: Book):
        """
        Adds a book (Book, EBook, or PrintBook instance) to the library's collection.

        Args:
            book (Book): An instance of Book or its derived classes.
        """
        if isinstance(book, Book): # Ensure that the object being added is a Book or a subclass of Book
            self.books.append(book)
            print(f"Added '{book.title}' to the library.")
        else:
            print("Error: Only Book instances (or derived classes) can be added to the library.")

    def list_books(self):
        """
        Prints the details of each book currently stored in the library.
        It uses the __str__ method of each book object for display.
        """
        if not self.books:
            print("The library is currently empty.")
            return

        print("\n--- Books in the Library ---")
        for book in self.books:
            print(book) # This will automatically call the __str__ method of the respective book object
        print("----------------------------")

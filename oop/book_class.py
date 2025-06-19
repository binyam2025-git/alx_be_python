"""
This script defines the Book class, demonstrating the use of Python's
magic methods: __init__ (constructor), __del__ (destructor),
__str__ (informal string representation), and __repr__ (official string representation).
"""

class Book:
    """
    Represents a book with a title, author, and publication year.
    Demonstrates the use of __init__, __del__, __str__, and __repr__ magic methods.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Constructor method to initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        #print(f"Book '{self.title}' created.") # Optional: for demonstrating creation

    def __del__(self):
        """
        Destructor method, called when the Book object is about to be destroyed.
        Prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns the informal string representation of the Book object.
        This is typically what is seen by end-users (e.g., when using print()).

        Returns:
            str: A string in the format "(title) by (author), published in (year)".
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns the official string representation of the Book object.
        This representation should ideally be unambiguous and, if possible,
        allow for recreation of the object.

        Returns:
            str: A string that would recreate the Book instance,
                 e.g., "Book('1984', 'George Orwell', 1949)".
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Example usage (for direct testing, though main.py will be used for official testing):
if __name__ == "__main__":
    print("--- Testing Book Class directly ---")
    my_test_book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
    print(my_test_book)
    print(repr(my_test_book))
    # When my_test_book goes out of scope or is explicitly deleted, __del__ will be called.
    del my_test_book
    print("--- Direct testing complete ---")

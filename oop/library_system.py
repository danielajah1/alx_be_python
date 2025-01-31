class Book:
    """Base class representing a book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an E-Book."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a Print Book."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count  # Number of pages

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Library class using composition to manage a collection of books."""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a book to the library."""
        self.books.append(book)

    def list_books(self):
        """Lists all books in the library."""
        if not self.books:
            print("The library has no books.")
        else:
            for book in self.books:
                print(book)

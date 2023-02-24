"""
BookCollection Class
"""

import csv
from operator import attrgetter
from book import Book


class BookCollection:
    """Represents collection of books."""

    def __init__(self):
        """Initializes Bookcollection instance."""
        self.books = []  # class instance variable that stores the value

    def __str__(self):
        """Returns a string representation."""
        books = [book.title for book in self.books]
        return "\n".join(books)

    def load_books(self, csv_file):
        """Add contents from csv file into Book objects in the list."""
        with open(csv_file, "r") as in_file:
            book_reader = csv.reader(in_file)
            for row in book_reader:
                if row[-1] == "c":  # Iterating to check the status of the book
                    row[-1] = True  # Changes to boolean to use Book class function
                else:
                    row[-1] = False
                books = Book(row[0], row[1], int(row[2]), row[3])  # Stores in a Book object accordingly
                self.books.append(books)

    def add_book(self, book):
        """Add a single Book object to the books attribute."""
        self.books.append(book)

    def get_number_of_required_books(self):
        """Get number of unread books."""
        required_books = 0
        for book in self.books:
            if not book.is_read:
                required_books += 1
        return required_books

    def get_required_pages(self):
        """Get number of unread book pages."""
        unread_pages = 0
        for i in range(len(self.books)):
            if not self.books[i].is_read:  # If the book is required to be read
                count_pages = self.books[i].number_of_pages
                unread_pages += int(count_pages)
        return unread_pages

    def sort(self, key):
        """Sorts book object by key attribute."""
        self.books.sort(key=attrgetter(key))  # Does not return anything, sorts the books according to key

    def save_books(self):
        """Save books stored in a list back to csv file."""
        with open("books.csv", "w", newline="") as new_book:  # newline makes the rows locate after each other
            writer = csv.writer(new_book)
            for book in self.books:
                if book.is_read:
                    status = "c"  # Convert boolean value to original string
                else:
                    status = "r"
                writer.writerow([book.title, book.author, book.number_of_pages, status])  # Save book in correct format

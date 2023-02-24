"""
Reading Tracker 1.0 with classes
"""

from book import Book
from bookcollection import BookCollection


CHOICES = ["L", "A", "M", "Q"]  # Constant of menu choices


def main():
    book_collection = BookCollection()  # Calls the class BookCollection
    book_collection.load_books("books.csv")
    print("Reading Tracker 1.0 - by Suyeon Yang")
    print("{} books loaded".format(len(book_collection.books)))
    user_input = ""
    while user_input != "Q":  # Iterates until user chooses to quit the program
        print_menu()  # Prints the user choice menu after each task
        user_input = input(">>>").upper()  # Uppercase to match the list of constant
        if user_input == "L":  # A menu choice that list all the books
            print_books(book_collection)
            required_books = book_collection.get_number_of_required_books()
            required_pages = book_collection.get_required_pages()
            print("You need to read {} pages in {} books.".format(required_pages, required_books))
        elif user_input == "A":  # A menu choice that lets user add book
            add_book(book_collection)
        elif user_input == "M":  # A menu choice that lets user mark a book as completed
            mark_book_as_completed(book_collection)
        elif user_input not in CHOICES:  # Error-checking for invalid menu choice
            print("Invalid menu choice.")
    book_collection.save_books()  # Saves book if the user selects "Q" == quit
    print("{} books saved to books.csv".format(len(book_collection.books)))


def print_menu():
    """Print menu choices for user input."""
    print("Menu:\n L - List all books\n A - Add new book \n M - Mark book as completed\n Q - Quit")


def print_books(book_collection):
    """Print Book objects in an orderly formatted strings."""
    book_number = 0  # indexing purpose of the book
    for book in book_collection.books:
        book_number += 1
        if not book.is_read:
            status = "*"  # To mark a book as required
        elif book.is_read:
            status = " "
        print("{}{}. {:<40} by {:<18} {:>5} pages".format(status, book_number, book.title, book.author,
                                                          book.number_of_pages))


def add_book(book_collection):
    """Add a validated Book object to the collection."""
    book_title = input("Title: ")
    while not book_title:
        print("Input can not be blank")
        book_title = input("Title: ")
    book_author = input("Author: ")
    while not book_author:
        print("Input can not be blank")
        book_author = input("Author: ")
    while True:
        try:
            book_pages = int(input("Pages: "))
            assert book_pages > 0  # To avoid input of negative integer
            break
        except ValueError:
            print("Invalid input; enter a valid number")
        except AssertionError:
            print("Number must be > 0")

    book_collection.add_book(Book(book_title, book_author, book_pages, False))  # Adds a new book object
    print("{} by {}, ({}) added to Reading Tracker.".format(book_title, book_author, book_pages))


def mark_book_as_completed(book_collection):
    """Validate user book number input."""
    while True:
        try:
            book_number_input = int(input("Enter the number of book to mark as completed: "))
            assert book_number_input > 0  # To avoid input of negative integer
            if book_number_input > len(book_collection.books):  # To avoid user input bigger than number of saved books
                raise Exception
            break
        except ValueError:
            print("Invalid input; enter a valid number")
        except AssertionError:
            print("Number must be > 0")
        except Exception as e:
            print("Invalid book number")

    book_number = book_number_input - 1  # For the list index starts with 0

    book = book_collection.books[book_number]  # Calls the book object of corresponding book number
    is_read = book_collection.books[book_number].is_read
    if is_read:  # Checks if whether a book is completed or not
        print("That book is already completed")
    else:
        print("{} by {} completed!".format(book.title, book.author))
        book_collection.books[book_number].is_completed()  # Changes the status to completion


if __name__ == '__main__':
    main()


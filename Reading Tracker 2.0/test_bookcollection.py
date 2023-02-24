"""Tests for BookCollection class."""
from bookcollection import BookCollection
from book import Book


def run_tests():
    """Test BookCollection class."""

    # Test empty BookCollection (defaults)
    print("Test empty BookCollection:")
    book_collection = BookCollection()
    print(book_collection)
    assert not book_collection.books  # PEP 8 suggests not using len() to test for empty lists

    # Test loading books
    print("\nTest loading books:")
    book_collection.load_books('books.csv')
    print(book_collection)
    assert book_collection.books  # assuming CSV file is non-empty, length should be non-zero

    # Test adding a new Book with values
    print("\nTest adding new book:")
    book_collection.add_book(Book("War and Peace", "William Shakespeare", 999, False))
    print(book_collection)

    # Test sorting books
    print("\nTest sorting - author:")
    book_collection.sort("author")
    print(book_collection)

    print("\nTest sorting - title:")
    book_collection.sort("title")
    print(book_collection)

    print("\nTest sorting - pages:")
    book_collection.sort("number_of_pages")
    print(book_collection)

    print("\nTest get_required_pages():")
    new_book_collection = BookCollection()
    new_book_collection.load_books("books.csv")
    print(new_book_collection.get_required_pages())

    book_collection.save_books()


run_tests()

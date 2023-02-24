"""Tests for Book class."""
from book import Book


def run_tests():
    """Test Book class."""

    # Test empty book (defaults)
    print("Test empty book:")
    default_book = Book()
    print(default_book)
    assert default_book.title == ""
    assert default_book.author == ""
    assert default_book.number_of_pages == 0
    assert not default_book.is_completed()

    # Test initial-value book
    print("Test initial-value book:")
    new_book = Book("Fish Fingers", "Dory", 501, True)
    print(new_book)

    assert new_book.title == "Fish Fingers"
    assert new_book.author == "Dory"
    assert new_book.number_of_pages == 501
    assert new_book.is_completed

    # Test mark_required()
    assert not new_book.mark_required()

    # Test is_long()
    assert new_book.is_long()
    print("Is the {} book long? {}".format(new_book.title, new_book.is_long()))
    assert not default_book.is_long()
    print("Is the {} book long? {}".format(default_book.title, default_book.is_long()))

    # More appropriate tests
    print("Test another-book:")
    another_book = Book("Harry Potter", "J.K Rowling", 507, False)
    print(another_book)

    assert another_book.title == "Harry Potter"
    assert another_book.author == "J.K Rowling"
    assert another_book.number_of_pages == 507
    assert not another_book.is_completed()


run_tests()

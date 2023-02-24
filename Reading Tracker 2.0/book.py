"""
Book Class
"""


class Book:
    """Represent a book object."""
    def __init__(self, title="", author="", number_of_pages=0, is_read=False):  # A book has a title, author, and pages
        """Initialize a book instance."""
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.is_read = is_read

    def __str__(self):
        """Returns a string representation."""
        return "{} by {}, {} pages".format(self.title, self.author, self.number_of_pages)

    def __repr__(self):
        """Returns a sting representation."""
        return self.__str__()

    def is_completed(self):
        """Determines the status of a book."""
        self.is_read = True

    def mark_required(self):
        """Determines the status of a book."""
        self.is_read = False

    def is_long(self):
        """Determine if a book is considered long."""
        if self.number_of_pages > 500:
            return True
        return False

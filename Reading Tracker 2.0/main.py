"""
Name: Suyeon Yang
Date: 28 May 2021
Brief Project Description: Reading Tracker 2.0
GitHub URL: https://github.com/JCUS-CP1404/assignment-2-reading-tracker-suyeon-yang
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button

from bookcollection import BookCollection


class ReadingTrackerApp(App):
    """Main program - Kivy app combining classes and Kivy."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        book_collection = BookCollection()
        book_collection.load_books("books.csv")
        self.book_collection = book_collection
        self.books = book_collection.books

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Reading Tracker 2.0"
        self.root = Builder.load_file("app.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from Book objects and add them to the GUI."""
        self.root.ids.book_list.clear_widgets()
        for book in self.books:
            temp_button = Button(text=str(book))
            self.root.ids.book_list.add_widget(temp_button)

    def sort_books(self, key):
        """Sorts Book objects according to the key."""
        if key == "Title":
            self.book_collection.sort("title")
        elif key == "Author":
            self.book_collection.sort("author")
        elif key == "Pages":
            self.book_collection.sort("number_of_pages")
        elif key == "Completed":
            self.book_collection.sort("is_read")
        self.create_widgets()


if __name__ == '__main__':
    ReadingTrackerApp().run()

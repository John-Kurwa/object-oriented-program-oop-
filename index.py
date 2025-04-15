# assignment 1
class Book:  
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self._pages = pages  # Encapsulated attribute
        self.genre = genre
        self._is_open = False

    def open_book(self):
        if not self._is_open:
            self._is_open = True
            print(f"Opening '{self.title}' by {self.author}.")
        else:
            print(f"'{self.title}' is already open.")

    def close_book(self):
        if self._is_open:
            self._is_open = False
            print(f"Closing '{self.title}'.")
        else:
            print(f"'{self.title}' is already closed.")

    def read(self):
        if self._is_open:
            print(f"Reading {self._pages} pages of thrilling {self.genre} content...")
        else:
            print("You need to open the book first!")

    # Encapsulation: controlled access to pages
    def get_pages(self):
        return self._pages

    def set_pages(self, pages):
        if pages > 0:
            self._pages = pages
        else:
            print("Page count must be greater than zero.")

# Subclass: EBook (inherits from Book)
class EBook(Book):
    def __init__(self, title, author, pages, genre, file_size_mb):
        super().__init__(title, author, pages, genre)
        self.file_size_mb = file_size_mb
        self.downloaded = False

    def download(self):
        if not self.downloaded:
            self.downloaded = True
            print(f"Downloading '{self.title}'... ({self.file_size_mb}MB)")
        else:
            print(f"'{self.title}' is already downloaded.")

    # Polymorphism: overriding the read method
    def read(self):
        if not self.downloaded:
            print("Please download the book before reading.")
        elif not self._is_open:
            print("Open the eBook before reading.")
        else:
            print(f"Reading '{self.title}' on your device...")

# Example usage
physical_book = Book("Kifo Kisimani", "Kithaka wa Mberia", 105, "Drama")
physical_book.open_book()
physical_book.read()
physical_book.close_book()

print()

ebook = EBook("Betrayal in the City", "Francis Imbuga", 80, "Drama", 2)
ebook.read()         # Will prompt to download
ebook.download()
ebook.open_book()
ebook.read()

# Activity 2: Polymorphism challenge
# Base class
class Transport:
    def travel(self):
        # This method will be customized by specific transport types
        print("The transport is in motion...")

# Specific class for a car
class BMW(Transport):
    def travel(self):
        print("🚘 Rolling down the highway...")

# Specific class for a plane
class Jet(Transport):
    def travel(self):
        print("🛫 Soaring through the clouds...")

# Specific class for a boat
class Yacht(Transport):
    def travel(self):
        print("🛥️ Cruising over the waves...")

# Specific class for a bicycle
class MountainBike(Transport):
    def travel(self):
        print("🚵‍♂️ cycling along the town...")

def test_transport_modes(modes):
    for mode in modes:
        mode.travel()

# Create a list of different transport modes
fleet = [BMW(), Jet(), Yacht(), MountainBike()]

# Run the test
test_transport_modes(fleet)

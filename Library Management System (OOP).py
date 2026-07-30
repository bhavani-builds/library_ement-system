class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        print("-" * 30)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'"{book.title}" added successfully.')

    def show_books(self):
        if not self.books:
            print("No books in the library.")
            return

        print("\nLibrary Books")
        print("=" * 30)
        for book in self.books:
            book.display()

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print(f'You borrowed "{book.title}".')
                else:
                    print("Book is already borrowed.")
                return
        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print(f'You returned "{book.title}".')
                else:
                    print("Book was not borrowed.")
                return
        print("Book not found.")


# Inheritance
class DigitalBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    # Polymorphism
    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Digital Book : {self.title}")
        print(f"Author       : {self.author}")
        print(f"File Size    : {self.file_size} MB")
        print(f"Status       : {status}")
        print("-" * 30)


# Main Program
library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Add Digital Book")
    print("3. Show Books")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Book Title: ")
        author = input("Author: ")
        library.add_book(Book(title, author))

    elif choice == "2":
        title = input("Book Title: ")
        author = input("Author: ")
        size = float(input("File Size (MB): "))
        library.add_book(DigitalBook(title, author, size))

    elif choice == "3":
        library.show_books()

    elif choice == "4":
        title = input("Enter book title: ")
        library.borrow_book(title)

    elif choice == "5":
        title = input("Enter book title: ")
        library.return_book(title)

    elif choice == "6":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Try again.")
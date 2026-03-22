class Book:
    def __init__(self, name):
        self.name = name
        self.available = True


class Member:
    def __init__(self, name):
        self.name = name


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        name = input("Enter book name: ")
        b = Book(name)
        self.books.append(b)
        print("Book added")

    def show_books(self):
        print("\nBooks:")
        for b in self.books:
            status = "Available" if b.available else "Issued"
            print(b.name, "-", status)

    def issue_book(self):
        name = input("Enter book to issue: ")
        for b in self.books:
            if b.name == name and b.available:
                b.available = False
                print("Book issued")
                return
        print("Book not available")

    def return_book(self):
        name = input("Enter book to return: ")
        for b in self.books:
            if b.name == name:
                b.available = True
                print("Book returned")
                return


lib = Library()

while True:
    print("\n--- LIBRARY MENU ---")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        lib.add_book()
    elif ch == 2:
        lib.show_books()
    elif ch == 3:
        lib.issue_book()
    elif ch == 4:
        lib.return_book()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
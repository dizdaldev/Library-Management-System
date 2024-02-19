import datetime

class Book:
    def __init__(self, title, author, release_date, num_pages):
        self.title = title
        self.author = author
        self.release_date = release_date
        self.num_pages = num_pages

class Library:
    def __init__(self):
        self.file_path = "books.txt"
        try:
            self.file = open(self.file_path, "a+")
        except IOError as e:
            print(f"Error: Unable to open file - {e}")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for line in lines:
            book_info = line.split(',')
            title, author, release_date, num_pages = book_info
            print(f"Title: {title}, Author: {author}, Release Date: {release_date}, Pages: {num_pages}")


    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_date = input("Enter release date (YYYY-MM-DD): ")
        num_pages = input("Enter number of pages: ")

        try:
            release_date = datetime.datetime.strptime(release_date, '%Y-%m-%d')
            num_pages = int(num_pages)
            if num_pages <= 0:
                raise ValueError("Number of pages must be a positive integer.")
        except ValueError as ve:
            print(f"Invalid input: {ve}")
            return

        book = Book(title, author, release_date, num_pages)
        self.file.write(f"{book.title},{book.author},{book.release_date},{book.num_pages}\n")
        print("Book added successfully!")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")

        lines = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()

        for line in lines:
            if title_to_remove not in line:
                self.file.write(line)

        print(f"Book '{title_to_remove}' removed successfully!")

    def update_book(self):
        title_to_update = input("Enter the title of the book to update: ")

        lines = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()

        for line in lines:
            if title_to_update in line:
                new_title = input("Enter new title: ")
                new_author = input("Enter new author: ")
                new_release_date = input("Enter new release date (YYYY-MM-DD): ")
                new_num_pages = input("Enter new number of pages: ")

                updated_info = f"{new_title},{new_author},{new_release_date},{new_num_pages}\n"
                self.file.write(updated_info)
                print(f"Book '{title_to_update}' updated successfully!")
            else:
                self.file.write(line)

# Create an object named "lib" with the Library class
lib = Library()

# Menu
while True:
    print("*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Update Book")
    print("5) Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        lib.update_book()
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

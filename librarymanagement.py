class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        # Check for exact duplicate (same title and author)
        for book in self.books:
            if book.title.lower() == title.lower() and book.author.lower() == author.lower():
                print(f" Book '{title}' by {author} already exists in the library.")
                return

        book = Book(title, author)
        self.books.append(book)
        print(f" Book '{title}' by {author} added.")

    def view_books(self):
        if not self.books:
            print(" No books in the library.")
        else:
            print("\n--- Library Books ---")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")
            print("---------------------")

    def _find_book(self, title, author=None):
        """Helper method to find a book, optionally by author."""
        matching_books = []
        for book in self.books:
            if book.title.lower() == title.lower():
                if author:
                    if book.author.lower() == author.lower():
                        matching_books.append(book)
                else:
                    matching_books.append(book)
        return matching_books

    def borrow_book(self, title):
        matching_books = self._find_book(title)

        if not matching_books:
            print(" Book not found in the library.")
        elif len(matching_books) == 1:
            book = matching_books[0]
            if book.available:
                book.available = False
                print(f" You borrowed '{book.title}' by {book.author}.")
            else:
                print(f" Book '{book.title}' by {book.author} is currently borrowed.")
        else:
            print(f"Multiple books found with title '{title}'. Please specify the author.")
            for i, book in enumerate(matching_books, 1):
                print(f"{i}. {book.title} by {book.author}")
            
            author_input = input("Enter the author's name to specify: ").strip()
            found_specific_book = False
            for book in matching_books:
                if book.author.lower() == author_input.lower():
                    if book.available:
                        book.available = False
                        print(f" You borrowed '{book.title}' by {book.author}.")
                        found_specific_book = True
                        break
                    else:
                        print(f" Book '{book.title}' by {book.author} is currently borrowed.")
                        found_specific_book = True
                        break
            if not found_specific_book:
                print(f" No book found with title '{title}' and author '{author_input}'.")


    def return_book(self, title):
        matching_books = self._find_book(title)

        if not matching_books:
            print(" Book not found in the library.")
        elif len(matching_books) == 1:
            book = matching_books[0]
            if not book.available:
                book.available = True
                print(f" You returned '{book.title}' by {book.author}.")
            else:
                print(f" Book '{book.title}' by {book.author} was not borrowed.")
        else:
            print(f"Multiple books found with title '{title}'. Please specify the author.")
            for i, book in enumerate(matching_books, 1):
                print(f"{i}. {book.title} by {book.author}")

            author_input = input("Enter the author's name to specify: ").strip()
            found_specific_book = False
            for book in matching_books:
                if book.author.lower() == author_input.lower():
                    if not book.available:
                        book.available = True
                        print(f" You returned '{book.title}' by {book.author}.")
                        found_specific_book = True
                        break
                    else:
                        print(f" Book '{book.title}' by {book.author} was not borrowed.")
                        found_specific_book = True
                        break
            if not found_specific_book:
                print(f" No book found with title '{title}' and author '{author_input}'.")

    def search_book(self, query):
        found_books = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                found_books.append(book)
        
        if not found_books:
            print(f" No books found matching '{query}'.")
        else:
            print(f"\n--- Search Results for '{query}' ---")
            for i, book in enumerate(found_books, 1):
                print(f"{i}. {book}")
            print("------------------------------------")

    def remove_book(self, title, author=None):
        matching_books = self._find_book(title)

        if not matching_books:
            print("Book not found in the library.")
        elif len(matching_books) == 1:
            book_to_remove = matching_books[0]
            self.books.remove(book_to_remove)
            print(f" Book '{book_to_remove.title}' by {book_to_remove.author} has been removed.")
        else:
            print(f"Multiple books found with title '{title}'. Please specify the author to remove.")
            for i, book in enumerate(matching_books, 1):
                print(f"{i}. {book.title} by {book.author}")
            
            author_input = input("Enter the author's name to specify: ").strip()
            found_specific_book = False
            for book in matching_books:
                if book.author.lower() == author_input.lower():
                    if not book.available: # Optional: prevent removal if borrowed
                        print(f" Cannot remove '{book.title}' by {book.author} as it is currently borrowed. Please return it first.")
                    else:
                        self.books.remove(book)
                        print(f"🗑️ Book '{book.title}' by {book.author} has been removed.")
                    found_specific_book = True
                    break
            if not found_specific_book:
                print(f" No book found with title '{title}' and author '{author_input}'.")


def main():
    library = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Book")  # New option
        print("6. Remove Book")  # New option
        print("7. Exit")         # Updated exit option

        choice = input("Enter your choice (1–7): ").strip()

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            title = input("Enter the title of the book to borrow: ")
            library.borrow_book(title)

        elif choice == "4":
            title = input("Enter the title of the book to return: ")
            library.return_book(title)
        
        elif choice == "5": # Search
            query = input("Enter title or author to search: ")
            library.search_book(query)

        elif choice == "6": # Remove
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)

        elif choice == "7": # Exit
            print(" Exiting Library System. Bye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
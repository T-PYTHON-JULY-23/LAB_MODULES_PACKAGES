def add_book(library, title, author, isbn):
    """Add a new book to the library."""
    for book in library:
        if book["isbn"] == isbn:
            print("Error: Book with the same ISBN already exists.")
            return
    new_book = {"title": title, "author": author, "isbn": isbn, "available": True}
    library.append(new_book)
    print(f"Book '{title}' by {author} (ISBN: {isbn}) added to the library.")


def remove_book(library, isbn):
    
    for book in library:
        if book["isbn"] == isbn:
            library.remove(book)
            print(f"Book '{book['title']}' by {book['author']} (ISBN: {isbn}) removed from the library.")
            return
    print("Error: Book with the given ISBN does not exist in the library.")

def check_out_book(library, isbn):
   
    for book in library:
        if book["isbn"] == isbn:
            if book["available"]:
                book["available"] = False
                print(f"Book '{book['title']}' by {book['author']} (ISBN: {isbn}) checked out.")
                return
            else:
                print(f"Error: Book '{book['title']}' by {book['author']} (ISBN: {isbn}) is not available.")
                return
    print("Error: Book with the given ISBN does not exist in the library.")

def return_book(library, isbn):
    
    for book in library:
        if book["isbn"] == isbn:
            book["available"] = True
            print(f"Book '{book['title']}' by {book['author']} (ISBN: {isbn}) returned to the library.")
            return
    print("Error: Book with the given ISBN does not exist in the library.")

def display_books(library):
    
    for book in library:
        status = "Available" if book["available"] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")

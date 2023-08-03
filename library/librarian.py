def add_book(library : dict, title : str, author : str, isbn : str ):
    if isbn in library :
        print(f"Book with ISBN {isbn} already exists in the library.")
    else:
        book = {"title": title , "author": author ,"isbn": isbn, "available":True}
        library [isbn] = book #library.update...


def remove_book(library, isbn) : 
    if isbn in library:
        del library[isbn]
        print("deleted book successfully")
    else :
        print("the book is not found")

def check_out_book(library : dict, isbn : str):
    book = library.get(isbn)
    if book and book ["available"] :
        book["available"] == False
    else :
        print("book is not available for checking out ")

def return_book(library : dict, isbn : str):
    book = library.get(isbn)
    if book and book ["available"] :
        book["available"] == False
    else :
        print("book is already returned ")

def display_books(library):
    for isbn, book in library.items():
        availability = "Available" if book['available'] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {isbn}) - {availability}")
    

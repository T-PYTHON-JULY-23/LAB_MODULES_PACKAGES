

def add_book(library, title, author, isbn):
    if isbn in library:
        print("The book is  ")
    else:
        book={"title": title, "auther":author , "available": True}
        library[isbn] = book
        print("book added")

def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
        print("deleted book succssfully")
    else:
        print("the boob is not found")

def check_out_book(library, isbn):
    book = library.get(isbn)
    if book and book["available"] == True:
        book["available"]== False
        print("is alreadt checed out")
    else:
        print("book is not available for chacking out")
    
    
def return_book(library, isbn):
    book = library.get[isbn]
    if book and not book["available"] == True:
        book["available"]== False
    else:
        print("book is already returned")
    

def display_books(library):
    for book , isbn in library:
        available_phress=""
        if book["available"]:
            available_phress = "Available"
        else:
             available_phress = "Not Available"
        print(f"{book['title']} (ISBN:{isbn}) - {available_phress}")
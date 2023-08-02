def add_book(library : dict,title : str,author:str,isbn:str):
    if isbn not in library:
        book ={'title': title , 'author' : author , "isbn":isbn,"available":True}
        library[isbn] = book
    else:
        print(f"Book with isban {isbn} is exists in the libary")

def remove_book(library, isbn):
    if isbn not in library:
        print(f"the book with ISBAN {isbn} not exists")
    else:
        del[isbn]

def check_out_book(library : dict, isbn : str):
    book = library.get(isbn)
    if book and book["available"]:
        book["available"] = False
        print(f"Book with isban {isbn} is checked out")
    else:
         print("Book is not available for checkout")

def return_book(library:dict, isbn:str):
    if isbn not in library:
        print(f"Book with isban {isbn} is not exists in the libary")
    else:
         library[isbn]["available"]=True

def display_books(library):
    for book in library.values():
        exists ="Available" if book["available"] else "Not available"
        print(f"{book['title']} by {book['author']} (ISBN:{book['isbn']})- {exists}")

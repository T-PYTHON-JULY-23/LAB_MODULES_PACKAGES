def add_book(library:dict, title:str, author:str, isbn:str):
    if isbn not in library:
        book = {"title" :title , "author" :author,"available" : True }
        library[isbn] = book
    else:
        print("The book already added in the library")


def remove_book(library:dict, isbn:str):
    if isbn in library:
        del library [isbn]
        print(f"the book with ISBN: ({isbn})deleted!")
    else:
        print(f"the book with ISBN: ({isbn}) not exists in library")



def check_out_book(library:dict, isbn:str):
    book = library.get(isbn)
    if book and book["available"]:
        book["available"] = False
        print(f"Book with{isbn} is checked out")
    else:
        print("Book is not available for checking out")



def return_book(library:dict, isbn:str):
    book = library.get(isbn)
    if book and book["available"]:
        book["available"] = True
    else:
        print("Book is already return")





def display_books(library:dict):
    for book in library.values():
        if book["available"]:
            f = "available"
        else:
            f = "Not available"
            print(f"{book['title']} by {book['author']} {book['isbn']}) -'{f} ")
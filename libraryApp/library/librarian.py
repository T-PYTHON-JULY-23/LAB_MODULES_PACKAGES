     
def add_book(library:dict, title:str, author:str, isbn:str,available):  
    if isbn in library.items():
        print('There is a book with same ISBN\n')
        return 
    else:
        library[isbn]={'title':title,'author':author,'isbn':isbn,'available':available}
        print("the book successfully added")


def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
        print(f"the book with ISBN: ({isbn}) successfully deleted")
    else:
        print("book not found")


def check_out_book(library, isbn):
    book=library.get(isbn)
    if book and book["available"]:
        book["available"]= False
        print(f"{book['title']} by {book['author']} (isbn: {isbn}) - Checked out ")
    else:
        print("book is not available")
    
def return_book(library, isbn):
    book=library.get(isbn)
    if book and book["available"]==False:
        book["available"]= True
    else:
        print("book is alredy returnd")


def display_books(library): 
    for isbn, book in library.items():
        if book['available']:
            ava="available"
        else:
            ava="Checked out"
        print(f"{book['title']} by {book['author']} (isbn: {isbn}) -'{ava} ")
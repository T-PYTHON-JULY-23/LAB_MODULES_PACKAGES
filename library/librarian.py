def add_book(library:dict, title:str, author:str, isbn:str):
    if isbn in library:
      print(f"actuly we already have {library[isbn]['title']} book")
    else:
        library.update({isbn : {"title" : title, "author" : author, "isbn": isbn, "available": True}})
        print(f"{library[isbn]['title']} is added")


def remove_book(library:dict, isbn:str):
    if isbn in library:
        print(f"done!, {library[isbn]['title']} has been deleted.")
        del library[isbn]
    else:
        print("sorry the book you want to delete is not registerd or already has been deleted.")


def check_out_book(library:dict, isbn:str):
    if isbn in library:
        if library[isbn]['available']:
            library[isbn]['available'] = False
            print(f"{library[isbn]['title']} is available and check out is done!.")
        else:
            print(f"{library[isbn]['title']} is not available right now.")
    else:
        print("sorry the book you trying to barrow is not in the library.")


def return_book(library:dict, isbn:str):
    if not isbn in library or library[isbn]['available']:
        print("this book is not available")
    else:
        library[isbn]['available'] = True
        print(f"thank you for returning '{library[isbn]['title']}' book to the library, we hope you enjoyed reading the book")
        

def display_books(library:dict):
    for isbn in library.keys():
        if library[isbn]['available']:
            print(f"{library[isbn]['title']} by {library[isbn]['author']} (ISBN : {isbn}) - Available")
        else:
            print(f"{library[isbn]['title']} by {library[isbn]['author']} ({isbn}) - Checked Out")

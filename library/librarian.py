def add_book(library:dict,title:str, author:str, isbn:str):
    if isbn in library:
        return print(f'{isbn} is already exists in the library')
    else:
        library.update({isbn:{'title':title, 'author':author, 'isbn':isbn, 'available':True}})
        return print(f'{isbn} Added successfully')
def remove_book(library:dict, isbn:str):
    if not isbn in library:
        return print(f'{isbn} does not exist')
    else:
        del library[isbn]
        return print('Deleted')
def check_out_book(library:dict, isbn:str):
    book = library.get(isbn)
    if book and book['available'] == True:
         book['available'] = False
    else:
        return print('book is not avaibale for checking out')
def return_book(library, isbn):
    book = library.get(isbn)
    if book and not book['available'] == True:
         book['available'] = True
    else:
        return print(f'{isbn} does not exist')
def display_books(library:dict):
    for isbn, book in library.items():
        if book["available"] == True:
            available = 'available'
        else:
            available = 'Checked Out'
        print(f'{book["title"]} by {book["author"]}.(ISBN: {isbn}) - {available}')


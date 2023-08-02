
def addBook(library, title, author, isbn):
        if isbn in library:
            print(f"Book with ISBN {isbn} already exists")
        else:
            library[isbn] = {'title': title, 'author': author, 'isbn': isbn, 'available': True}


def removeBook(library, isbn):
    if isbn not in library:
        print(f"Book with ISBN {isbn} does not exist")
    else:
        del library[isbn]


def checkOutBook(library, isbn):
    if isbn not in library:
        print(f"Book with ISBN {isbn} does not exist")
    elif not library[isbn]['available']:
        print(f"Book with ISBN {isbn} is not available")
    else:
        library[isbn]['available'] = False


def returnBook(library, isbn):
    if isbn not in library:
        print(f"Book with ISBN {isbn} does not exist")
    else:
        library[isbn]['available'] = True


def displayBooks(library):
    print("Books available in the library:")
    for book in library.values():
        print(f"{book['title']} by {book['author']}. ISBN: {book['isbn']}. Available: {book['available']}")

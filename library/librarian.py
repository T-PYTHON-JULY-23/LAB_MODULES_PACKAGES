
def add_book(library, title, author, isbn):
    
    library_val = library.value()
    if isbn in library_val:
        print("the book is already exists in the library,")
    else:
        library = {'title' :title, 
            'author' :author ,
            'isbn' :isbn,
            'available' : True }
        print("the book is added in the library,")

        
def remove_book(library, isbn):
    
    library_val = library.value()
    if isbn in library_val:
        del library(isbn)
        print("removed the book from the library")
    else:
        print("the book dosen't exists in the library,")

def check_out_book(library, isbn):

    library['available'] = False

    library_val = library.value()
    if isbn in library_val: 
        print("the book in the library,")
    else:
        print("the book is checked out")


def return_book(library, isbn):

    library['available'] = True
    library_val = library.value()
    if isbn in library_val: 
        print("the book returned to the library,")
    else:
        print("the book isn't returned yet")



def display_books(library):
    print("The original dictionary is : " + str(library))


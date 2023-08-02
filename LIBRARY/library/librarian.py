 




def add_book(library:dict, title:str, author:str, isbn:str):

  book = {"library":library,"title":title,author:"author",isbn:"isbn","available":True}
  if isbn in library:
    print("The book is available")

  else:
    library[isbn]=book
    print(f"{title} by {author} (ISBN: {isbn}) - Available")
 


def remove_book(library, isbn):

 if isbn in library :
    del library[isbn]
    print("book deleted successfuly!")
 else:
    print("The book is not Available ")

    

def check_out_book(library, isbn):
  if isbn in library:
    if library[isbn]['available']:
      library[isbn]['available'] = False
    print("the book is available and check out!.")
  else: 
   print("sorry , Book is not available")



def return_book(library:dict, isbn:str):
  if not isbn in library or library[isbn]['available']:
    print("this book is not available")
  else:
    library[isbn]['available'] = True
    print("The book has been returned")


def display_books(library):
   for isbn, book in library.items():
     print(f"{book['title']} by {book['author']} (ISBN: {isbn}) -{'Available'if book['Available'] else 'Checked Out'}")





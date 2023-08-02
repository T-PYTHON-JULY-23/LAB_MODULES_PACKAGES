
def add_book(library:dict, title:str, author:str, isbn:str):

 if isbn not in library:
   book= {'title':title,'author':author,'Available':True }
   library[isbn]=book
 else:
  print("The book is already added")

def remove_book(library:dict, isbn:str):
 
 if isbn in library:
  del library[isbn]
  print("book deleted successfuly!")
 else:
    print("book not available")
  

def check_out_book(library, isbn):
 book= library.get(isbn)
 if book and book["Available"]:
  book["Available"] = False
 else: 
  print("Book is not available")

def return_book(library, isbn):
 book= library.get(isbn)
 if book and not book["Available"]:
  book["Available"] = True
 else: 
  print("Book is already returend")

def display_books(library):
  for isbn, book in library.items():

   print(f"{book['title']} by {book['author']} (ISBN: {isbn}) -{'Available'if book['Available'] else 'Checked Out'}")
 


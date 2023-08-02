import dateOP
from library.librarian import *
from library import librarian

dateOP.print_date()
library = {
  "9780316769174": {
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger",   
    "isbn": "9780316769174",
    "available": True  
  },
  "9780446310789": {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",      
    "isbn": "9780446310789",
    "available": True  
  },   
  "9780451524935": {
    "title": "1984",  
    "author": "George Orwell",       
    "isbn": "9780451524935",
    "available": True  
  }      
}

check_out_book(library, "9780316769174")
display_books(library)


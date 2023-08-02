import dateOP
dateOP.current_date()
from library import librarian
library = {}

#add book
librarian.add_book(library, "Rish dad and poor dad", "Abdulmalik", "12345")
librarian.add_book(library, "Harry Potter", "Chrisitina", "32423")
#check out book
librarian.check_out_book(library, "12345")

#return book
librarian.return_book(library, "12345")


librarian.display_books(library)
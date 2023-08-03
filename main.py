import dateOP # >>>> import dateOP module

dateOP.current_date() # >>> call the function that print the current date


#from library import librarian
from library.librarian import add_book, remove_book, check_out_book, return_book, display_books

library = {}
# Add books
add_book(library, 'The Catcher in the Rye', 'J.D. Salinger', '9780316769174')
add_book(library, 'To Kill a Mockingbird', 'Harper Lee', '9780446310789')
add_book(library, '1984', 'George Orwell', '9780451524935')
display_books(library)

# Check out a book
check_out_book(library, '9780316769174')
display_books(library)

# Return a book
return_book(library, '9780316769174')
display_books(library)
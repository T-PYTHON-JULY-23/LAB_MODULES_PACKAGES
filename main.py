from dateOP import data_time
from library import librarian

print("the date is: ",data_time())
library={}
librarian.add_book(library ,"The Catcher in the Rye","J.D. Salinger","9780316769174")
librarian.add_book(library,"To Kill a Mockingbird","Harper Lee","9780446310789")
librarian.add_book(library,"1984","George Orwell","9780451524935")
print("-"*30)
librarian.display_books(library)
print("-"*30)
librarian.check_out_book(library,"9780316769174")
print("-"*30)
librarian.display_books(library)
print("-"*30)
librarian.return_book(library,"9780316769174")
print("-"*30)
librarian.display_books(library)
print("-"*30)
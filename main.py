import dateOP 
import librarian as book
print("_"*20)
dateOP.date_op(" ")
print("_"*20)
library={}
book.add_book(library,"The Catcher in the Rye","J.D. Salinger", "9780316769174")
book.add_book(library,"To Kill a Mockingbird","Harper Lee","9780446310789")
book.add_book(library,"1984","George Orwell","9780451524935")
book.display_books(library)
print("_"*20)
book.check_out_book(library,"9780316769174")
book.display_books(library)
print("_"*20)
book.return_book(library,"9780316769174")
book.display_books(library)
print("_"*20)
book.remove_book(library,"9780316769174")
book.display_books(library)
from library import librarian






# use the function from librarian to add books, remove book, checkout a book, and display books .
library={}

librarian.add_book(library, "The Catcher ", "J.D. Salinger", "9780316769174")
librarian.add_book(library, "To Kill a Mockingbird ", "Harper Lee", "9780446310789")
librarian.add_book(library, "1984 ", "George Orwell", "9780451524935")

librarian.remove_book(library, "9780451524935")


librarian.check_out_book(library, "9780316769174")

librarian.check_out_book(library, "9780446310789")

librarian.return_book(library, "9780316769174")

librarian.display_books(library)






import dateOP
dateOP.current_date()


from library import librarian as lib
book={}
print("")
lib.add_book(book,"The Catcher in the Rye", "J.D. Salinger","9780316769174")
lib.add_book(book,"To Kill a Mockingbird", "Harper Lee","9780446310789")
lib.add_book(book,"1984", "George Orwell","9780451524935")
lib.display(book)
print()
lib.del_book(book,"9780316769174")
lib.display(book)
print()
lib.checkout_book(book,"9780451524935")
lib.display(book)
print()
lib.return_book(book,"9780451524935")
lib.display(book)
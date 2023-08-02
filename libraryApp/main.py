from library import librarian 

library={}
librarian.add_book(library, "To Kill a Mockingbird", "Harper Lee","9780446310789", True)
librarian.add_book(library, "The Catcher in the Rye", "J.D. Salinger","9780316769174",True)
librarian.add_book(library, "The Little Prince", "ANTOINE DE SAINT-EXUPERY ","9780146729637",True) 
librarian.check_out_book(library, "9780446310789")
print("\n")
librarian.check_out_book(library, "9780882921769")
print("\n")

librarian.display_books(library)
print("\n")

librarian.remove_book(library, "9780446310789")
print("\n")

librarian.display_books(library)
print("\n")

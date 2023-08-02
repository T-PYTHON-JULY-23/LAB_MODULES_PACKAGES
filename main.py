
import dataeOP 
from library import librarian

#Q1
dataeOP.current_date()


#Bouns



#add book
library = {}
librarian.add_book(library, "Zero to one", " Random House; Latest edition", "024003497X")
librarian.add_book(library, "Your next five moves", "Simon & Schuster", " 1982154802")
librarian.add_book(library, "Deep Work", "Piatkus Books", "0349411905")
librarian.add_book(library, "Atomic Habits", "Avery" ," 0735211299" )
librarian.add_book(library, "The Catcher in the Rye", "J.D. Salinger","9780316769174")
librarian.add_book(library, "To Kill a Mockingbird", "Harper Lee","9780446310789")

#check out book
librarian.check_out_book(library," 1982154802")

#rmove a book
librarian.remove_book(library, "024003497X")

#disply book
librarian.display_books(library)







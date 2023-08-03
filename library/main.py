from library import librarian
library = {}
librarian.add_book(library, "Dracula", "Bram", "9929394999")
librarian.add_book(library, "Frankenstein", "Mary Shelley", "882838488")
librarian.add_book(library, "The Moonstone", "Wilkie Collins", "772737377")
librarian.add_book(library, "The Invisible Man","H.G. Wells","662636366" )
librarian.add_book(library, "Emma", "Jane Austen","5525354555")

librarian.check_out_book(library,"9929394999")

librarian.remove_book(library, "882838488")

librarian.return_book(library, "882838488")

librarian.display_books(library)
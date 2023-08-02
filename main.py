from dateOP import *

# import dateOP

print(get_date())

# print(dateOP.get_date())


#bonus-----------------------------

from library import librarian

library = {}


librarian.add_book(library, "book1", "ahmed", "121212")

librarian.check_out_book(library, "121212")

librarian.check_out_book(library, "12212")

librarian.return_book(library, "121212")

# librarian.remove_book(library, "121212")
librarian.display_books(library)


import dateoOP as mydate
import Library.librarian as lib



###### first part 
mydate.day_today()
print("End of first Part")
print("-"*20)


book_stock={}

lib.add_book(book_stock,isbn='9780316769174',title='The Catcher in the Rye',author='J.D. Salinger',is_avalible=True)
lib.add_book(book_stock,isbn='9780446310789',title='To Kill a Mockingbird',author='Harper Lee',is_avalible=True)
lib.add_book(book_stock,isbn='9780451524935',title='1984',author='George Orwell',is_avalible=True)

lib.display_books(book_stock)
lib.check_out_book(book_stock,'9780316769174')
lib.display_books(book_stock)
lib.return_book(book_stock,'9780316769174')
lib.display_books(book_stock)

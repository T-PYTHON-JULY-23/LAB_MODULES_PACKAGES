from dateOP import printDate  
from library.librarian import addBook, removeBook, checkOutBook, displayBooks, returnBook

library = {}

printDate()


# Add some books
addBook(library, 'The Catcher in the Rye', 'J.D. Salinger', '9780316769174')
addBook(library, 'To Kill a Mockingbird', 'Harper Lee', '9780446310789')
addBook(library, '1984', 'George Orwell', '9780451524935')

# Display the books
displayBooks(library)

# Checkout a book
checkOutBook(library, '9780316769174')

# Display the books after checkout
displayBooks(library)

# Return a book
returnBook(library, '9780316769174')

# Display the books after return
displayBooks(library) 

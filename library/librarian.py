def add_book(library, title, author, isbn):
    library[isbn] = {'title':title, 'author':author, 'isbn':isbn, 'available':True}    
        
def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
    else: 
        print(f"Book with ISBN {isbn} does not exist.") 
        
def check_out_book(library, isbn):  
    if isbn in library: 
        library[isbn]['available'] = False
    else: 
         print(f"Book with ISBN {isbn} is not available.")

def return_book(library, isbn):
    if isbn in library: 
        library[isbn]['available'] = True
    else:
        print(f"Book with ISBN {isbn} does not exist.")
        
def display_books(library):
    for data in library.values():
        availability = 'Available' if data['available'] else 'Checked Out'
        print(f"{data['title']} by {data['author']} ({data['isbn']}) - {availability}")
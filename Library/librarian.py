def add_book(library:dict, title:str, author:str, isbn:str):
    if isbn in library:
        book= {"title" : title, "author":author ,"available":True }
        library[isbn] = book 
        print( "the book is available")
    else:
        print ( "The book is added")
        
def remove_book(library:dict, isbn:str):
    if isbn in library:
     del library[isbn]
     print("the book is removed")  
    else: 
     print( "the booke is not avalible " )

def check_out_book(library:dict , isbn:str):
    book= library.get(isbn)

    if  book["avalbile"]==True:
       book["avalbile"] =False
       print("done check out")
    else:
       print(" book is already check out ")
       
def return_book (library:dict , isbn:str):
     if book["avalbile"]==True:
         print ("the book is returned")
     else:
         print("not exist")
    
def display_books (library:dict , isbn:str):
    if book in library.values():
      exist = book['available']
    else: "checked out"
    print(f"{book['title']} by {book['author']} ({book['isbn']}) - {exist}") 
    
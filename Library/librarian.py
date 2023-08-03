def add_book(library:dict, title:str, author:str, isbn:str):
    if isbn in library:
        
        print( "the book in  dictinary")
    else:
        book= {"title" : title, "author":author ,"available":True }
        library[isbn] = book 
        print ( "The book is added")
        
def remove_book(library:dict, isbn:str):
    if isbn in library:
     del library[isbn]
     print("the book is removed")  
    else: 
     print( "the booke is not avalible " )

def check_out_book(library:dict , isbn:str):
    book= library.get(isbn)

    if  book["available"]==True:
        book["available"] =False
        print("done check out")
    else:
       print(" book is already check out ")
       
def return_book (library:dict , isbn:str):
     book= library.get(isbn)
     if book["available"]==False:
         book["available"] =True
         print ("the book is returned")
     else:
         print("not exist")
    
def display_books (library:dict):
    for isbn, book in library.items():
     if book['available']==True:
        exist="available"
    
     else: 
      exist= "checked out"
     print(f"{book['title']} by {book['author']} ({isbn}) - {exist}") 
    
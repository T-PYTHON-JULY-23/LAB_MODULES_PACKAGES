
def add_book(library, title, author , isbn) :
   
   if isbn in library:
       print("this book in dictionry")
   else:
     book={ "title" :title ,"author":author,"avalbile":True}
     library [isbn]= book
     print(" book added ")
        
 

  
def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
        print("delted book")
    else:
        print("the book is not exist")
        
def check_out_book(library, isbn):
   book= library.get(isbn)
   
   if  book["avalbile"]==True:
       book["avalbile"] =False
       print("done check out")
  
   else:
       print(" book is already check out ") 
def return_book(library, isbn):
   book= library.get(isbn)
   
   if  book["avalbile"]==False:
       book["avalbile"] =True
       print("done retun")
   
   else:
       print(" book is already return") 
def display_books(library):
    

    for key,book_info in library.items():
        if book_info['avalbile']==True:
           avale="Available"
        else:
           avale="Checked Out"
     
        print(f"{book_info['title']} by {book_info['author']}  (ISBN: {key} ) - {avale}")
         


def add_book(library:dict,title:str, author:str, isbn:str):
    if isbn in library:
        print("The book is added")
    else:
        available=True
        book = {"title":title, "author":author,"isbn":isbn,"available":available}
        library[isbn] = book

def del_book(library:dict,isbn:str):
    if isbn in library:
        del library[isbn]
        print("The book is deleted")
    else:
        print("There is no book")
    

def checkout_book(library:dict,isbn:str):
    if isbn in library and  library[isbn]['available']==True:
        library[isbn]['available']=False
    else:
        print("Not exist")


def return_book(library:dict,isbn:str):
    if isbn in library and  library[isbn]['available']==False:
        library[isbn]['available']=True
    else:
        print('Not exist')
        





def display(library:dict):
    for key, values in library.items():
        res=""
        if values["available"] == True:
            res=("available")
        else:
            res=("Not available")
        print(f"{values['title']} by {values['author']} (ISBN: {values['isbn']}) - {res}")
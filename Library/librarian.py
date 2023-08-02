

def add_book(library:dict, title:str, author:str, isbn:str,is_avalible):
    if isbn in library.keys():
        print('There is a book with same ISBN\n')
        return

    library[isbn]={'title':title,'author':author,'avalible':is_avalible}

    

def remove_book(library:dict, isbn:str):
    if isbn in library.keys():
        del library[isbn]
    else:
        print('ISBN does not exist in the library\n')
    

def check_out_book(library:dict, isbn:str):
    if isbn in library.keys() and  library[isbn]['avalible']==True:
            library[isbn]['avalible']=False
    else:
        print('ISBN does not exist in the library or its checked out\n')

def return_book(library:dict, isbn:str):
    if isbn in library.keys() and  library[isbn]['avalible']==False:
        library[isbn]['avalible']=True
    else:
        print('ISBN does not exist in the library or its checked out\n')


def display_books(library:dict):
    for key ,value in library.items():
        x=None
        if value['avalible']==True:
            x='Available'
        else:
            x='Checked Out'
            
        print(f"{value['title']} by {value['author']} (ISBN: {key}) - {x}")
    print('')
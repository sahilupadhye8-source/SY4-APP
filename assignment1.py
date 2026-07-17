class library:
    def __init__(self):
        self.books=[]
        self.patrons=[]
        
    def add_book(self):
        books=input("enter book name:")
        self.books.append(books)
        print("book added")

    def add_patron(self):
        patron=input("enter patron name:")
        self.patrons.append(patron)

    def display_books(self):
        print("books in library:")
        print(self.books)

    def display_patrons(self):
        print("patrons in library:")
        print(self.patrons)     

l=library()

l.add_book()
l.add_patron()
l.display_books()
l.display_patrons()  

while(True):
    print ("\n1.add book")
    print("\n2.add patron")
    print("\n3.display all books")
    print("\n4.display all patrons")
    print ("\n5.end")

    ch=int(input("enter your choice:"))
    if (ch==1):
        l.add_book()
    elif(ch==2):
        l.add_patron()
    elif(ch==3):
        l.display_books()
    elif(ch==4):
        l.display_patrons()
    elif(ch==5):
        break 
                 
         




              
        
    
        
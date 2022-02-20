class Library:
    def __init__(self,listofbooks):
        self.books=listofbooks
    def displayavailablebooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print("\t"+"*"+book)
    def borrowbooks(self,bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname} Handle it properly and return it within 30days")
            self.books.remove(bookname)
            return True
        else:
            print("Sorry,Either This book is not available or book had already been issued to someone")
            return False 
    def returnbooks(self,bookname):
        self.books.append(bookname)
        print("Thanks for returning!")



class Student:
    def requestbook(self):
        self.book=input("Enter the book you want to borrow: ")
        return self.book
    def returnbook(self):
        self.book=input("Enter the book you want to return: ")
        return self.book



if __name__=="__main__":
    centrallibrary=Library(["DSA","CRIME THRILLER","IOTA","ELECTRICAL ENGINEERING"])
    student=Student()
    
    while(True):
        welcomemsg='''
        ===Welcome to Central Library
        Please choose an option:
        1. Listing all the books
        2. Request a book
        3. Add/Return a book
        4. Exit to the library
        '''
        print(welcomemsg)

        a=int(input("Enter your choice: "))
        if a==1:
            centrallibrary.displayavailablebooks()
        elif a==2:
            centrallibrary.borrowbooks(student.requestbook())
        elif a==3:
            centrallibrary.returnbooks(student.returnbook())
        elif a==4:
            print("Thanks for choosing Central Library!")
            exit()
        else:
            print("Invalid Option!")

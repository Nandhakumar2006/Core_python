class book:

    def __init__(self,bookid,bookname,bookprice):

        self.__bookid = bookid
        self.__bookname = bookname
        self.__bookprice = bookprice

    def set_bookid(self,bookid):
        self.bookid =bookid

    def set_bookname(self,bookname):
        self.__bookname =bookname

    def set_bookprice(self,bookprice):
        self.__bookprice =bookprice

    def get_bookid(self):
        return self.__bookid
    
    def get_bookname(self):
        return self.__bookprice
    def __str__(self):
        return "Book ID:"+str(self.__bookid)+" "+"Book Name:"+self.__bookname+" "+"Book Price:"+str(self.__bookprice)
    

#creating and storing objects in list books =[]

books=[]
n= int(input("how many books you want to enter"))

for i in range(n):
    bookid=int(input("enter the book id"))
    bookname=input("enter the book name")
    bookprice=int(input("enter the book price"))
    print() #print blank space
    book =book(bookid,bookname,bookprice)
    books.append(book)

#display book details

print("book details:\n")

for book in books:
    print("Book ID:",bookid.get_bookid())
    print("Book Name:",bookname.get_bookname())
    print("Book Price:",bookprice())
    print()
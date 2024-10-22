Books = {}
class Library:
    def __init__(self,Bookname,Book_ID):
        self.Bookname = Bookname
        self.Book_ID = Book_ID
    def Add_Book(Book):
        Books.update({Book.Book_ID:Book.Bookname})
        # print(f"Book '{Book.Bookname}' added to the library. Current books: {[book.Bookname for book in Books]}")
        print(f"Book ID:{Book.Book_ID} -> Book_Name:{Book.Bookname}")

    def Remove_Book(Book):
        Books.pop(Book.Book_ID)


    @staticmethod
    def Number_of_Books():
        Num_of_Books = len(Books)
        print(Num_of_Books)
    @staticmethod
    def Library_Books():
        # print(f"Current books: {[book.Bookname for book in Books]}")
        print(Books)

B1 = Library("Harry Potter",101)
Library.Add_Book(B1)
B2 =Library("The Hobbits",102)
Library.Add_Book(B2)
B3 = Library("Facebook Love",103)
Library.Add_Book(B3)
Library.Remove_Book(B2)
Library.Library_Books()
Library.Number_of_Books()
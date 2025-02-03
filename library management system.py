# step 1: define the class

class Book:

    def __init__(self, title, author, is_available):
        self.title = title
        self.author = author
        self.is_available = is_available

# step 2, define the method within the class

    def borrow_book(self):
        self.is_available = True
        if self.is_available:
            return f"You have borrowed {self.title} by {self.author}" 
        else:
            return f"Sorry, {self.title} by {self.author} is already borrowed"
        
        def return_book(self):
            if not self.is_available:
                self.is_available = True
                return f" book is available for borrowing"

# step 3, define the object

book1 = Book("The Alchemist", "Paulo Coelho", True)
book2 = Book("The 48 Laws of Power", "Robert Greene", True)
book3 = Book("The Art of War", "Sun Tzu", True)
book4 = Book("The 7 Habits of Highly Effective People", "Stephen Covey", True)
book5 = Book("Harry Potter", "J.K. Rowling", True)


# step 4, call the method
print(book1.borrow_book())
print(book2.borrow_book())
print(book3.borrow_book())  
print(book4.borrow_book())
print(book5.borrow_book())          

# step 5 run the code


class library (Book):

    def __init__(self, title, author, is_available):
        super().__init__(title, author, is_available)
        self.books = []
    
    
    book1 = Book("The Alchemist", "Paulo Coelho", True)
    book2 = Book("The 48 Laws of Power", "Robert Greene", True) 
    book3 = Book("The Art of War", "Sun Tzu", True) 
    book4 = Book("The 7 Habits of Highly Effective People", "Stephen Covey", True)
    book5 = Book("Harry Potter", "J.K. Rowling", True) 


    def add_book(self, book):
        self.books.append(book)
        return f"{book.title} has been added to the library"
    
    def list_books(self):
        return [book.title for book in self.books]
    
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return "Book not found"
    
    def borrow_book(self, title):
        book = self.find_book(title)
        if book:
            return book.borrow_book()
        return "Book not found"
    
    def return_book(self, title):
        book = self.find_book(title)
        if book:
            return book.return_book()
        return "Book not found"
    
    def exit_library(self):
        return "Thank you for visiting the library"
    
    def menu (self):
        while True:
            print("1. Add book")
            print("2. List books")
            print("3. Borrow book")
            print("4. Return book")
            print("5. Exit")

            choice = input("Enter choice: ")
            if choice == "1":
                title = input("Enter title: ")
                author = input("Enter author: ")
                is_available = input("Enter availability: ")
                book = Book(title, author, is_available)
                print(self.add_book(book))
            elif choice == "2":
                print(self.list_books())
            elif choice == "3":
                title = input("Enter title: ")
                print(self.borrow_book(title))
            elif choice == "4":
                title = input("Enter title: ")
                print(self.return_book(title))
            elif choice == "5":
                break
            else:
                print("Invalid choice")
        print(self.exit_library())


library = library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)

library.menu()

 



    
















            
    
            


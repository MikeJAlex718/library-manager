#JAM
#6/25/2025
#Stores several books properties and provides other useful methods

from book import Book

class LibraryManager:
    def __init__(self, books=None):
        self.books = []
        
        if books is not None:
            for curBook in books:
                self.books.append(curBook)
            
    #Displays all books' information in the library
    def displayAll(self):
        for book in self.books:
            print(book)
    
    #Adds the book parameter at the end of the list  
    def addBook(self,book):
        self.books.append(book)
    
    #Removes all occurences of book
    def removeBook(self, titleToRem):
        for book in self.books:
            if book.getTitle() == titleToRem:
                self.books.remove(book)
    
    #Sorts the books in the library by year and title
    def sortBooks(self):
        self.books.sort(key=lambda book: (-book.getYear(), book.getTitle()))
    
    #Finds if the book parameter exists, returns if does
    def findBook(self, targetTitle):
        for book in self.books:
            if book.getTitle() == targetTitle:
                return (f"{book.getTitle()} is in the library!")
        
        return (f"{targetTitle} not Found")
    
    #Finds if teh book parameter exists and marks it read
    def markBookRead(self, targetTitle):
        for book in self.books:
            if(book.getTitle()==targetTitle):
                book.markRead()
                print(f"{targetTitle} has been marked read successfully")
        
        return(f"{targetTitle} not found")
    
    #Saves the library of books into a text file
    def saveLibrary(self):
        with open("library.txt", "w") as file:
            for book in self.books:
                file.write(str(book))
    
    #Loads a text file storing several books' information
    def loadLibrary(self):
        try:
            with open("library.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts)==4:
                        title, author, year, didRead = parts    
                        self.books.append(Book(title, author, int(year), didRead.lower()=="true"))
        except FileNotFoundError:
            print("library.txt not found")
            self.books = []
        except Exception as e:
            print("Something went wrong")
            self.books = []
            
        self.books.sortBooks()
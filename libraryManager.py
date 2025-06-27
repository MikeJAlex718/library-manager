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
        if len(self.books) == 0:
            print("No book(s) to display\n")
        
        for book in self.books:
            print(book.toString())
    
    #Adds the book parameter at the end of the list  
    def addBook(self,book):
        self.books.append(book)
        print("Successfully Added your Book!\n")
    
    #Removes all occurences of book
    def removeBook(self, titleToRem):
        originalCount = len(self.books)
        self.books = [book for book in self.books if book.getTitle() != titleToRem]
        
        if len(self.books) < originalCount:
            print(f"Successfully Removed All Occurences of {titleToRem}\n")
        else:
            print(f"{titleToRem} not found in library\n")
    
    #Remove all books in library
    def removeAllBooks(self):
        self.books.clear()
        print("Succesfully removed all books!\n")
    
    #Sorts the books in the library by year and title
    def sortBooks(self):
        self.books.sort(key=lambda book: (-book.getYear(), book.getTitle()))
        print("Successfully Sorted your Library!\n")
    
    #Finds if the book parameter exists, returns if does
    def findBook(self, targetTitle):
        for book in self.books:
            if book.getTitle() == targetTitle:
                return (f"{book.getTitle()} is in the Library!\n")
        
        return (f"{targetTitle} not Found\n")
    
    #Finds if the book parameter exists and marks it read
    def markBookRead(self, targetTitle):
        for book in self.books:
            if(book.getTitle()==targetTitle):
                book.markRead()
                print(f"Successfully marked {targetTitle} read!")
                return
        
        print(f"{targetTitle} not found\n")
        return
    
    #Finds if the book parameter exists and marks it unread
    def markBookUnread(self, targetTitle):
        for book in self.books:
            if(book.getTitle()==targetTitle):
                book.markUnread()
                print(f"Successfully marked {targetTitle} unread!")
                return
        
        print(f"{targetTitle} not found\n")
        return
    
    #Saves the library of books into a text file
    def saveLibrary(self):
        with open("library.txt", "w") as file:
            for book in self.books:
                line = f"{book.getTitle()},{book.getAuthor()},{book.getYear()}, {book.getRead()}\n"
                file.write(line)
        
        print("Successfully saved your Library into a file!\n")
    
    #Loads a text file storing several books' information
    def loadLibrary(self):
        self.books = []
        try:
            with open("library.txt", "r") as file:
                for line in file:
                    #Determines if the file is empty
                    content = file.read().strip()
                    if content=="":
                        print("library.txt is empty, nothing to load.\n")
                        return
                    
                    parts = line.strip().split(",")
                    if len(parts)==4:
                        title, author, year, didRead = parts
                        book = Book(title, author, int(year), didRead=="True")
                        self.books.append(book)
                        
            print("Successfully Loaded a Library!")
        except FileNotFoundError:
            print("library.txt not found")
            self.books = []
        except Exception as e:
            print(f"Something went wrong [{e}]")
            self.books = []
            
        self.sortBooks()
        
    #Clear the data(s) of current text file
    def clearLibrary(self):
        self.books=[]
        with open("library.txt","w") as file:
            file.write("")
            
        print("library.txt has been cleared!\n")

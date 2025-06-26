#JAM
#6/25/2025
#Acts as a personal library with several options for the user

from book import Book
from libraryManager import LibraryManager

def main():
    print("Welcome to Your Personal Library\n")
    
    #Runs while the user decides not to exit (option 8)
    while True:
        print("1. Add a new book")
        print("2. Remove a book")
        print("3. View all books")
        print("4. Sort books by title & year")
        print("5. Search by Title")
        print("6. Save Library")
        print("7. Load Library")
        print("8. Exit")
        
        userChoice = input("Choose an option: ")
        curChoice = int(userChoice)
        
        #Runs while the user inputs terrible input
        while curChoice<1 or curChoice>7:
            userChoice = input("Choose an option: ")
        
        #Quits the loop early if the user wants to exit
        if curChoice==7:
            print("Thank you, come again!")
            break
        
        #Acts accordingly based on the user's choice
        userLibrary = LibraryManager()
        if curChoice==1:
            bookTitle = input("Enter the title of the book: ")
            bookAuthor = input("Enter the author of the book: ")
            bookYear = input("Enter the year the book was made: ")
            year = int(bookYear)
            
            hasRead = input("Have you read before?: ")
            hasRead = hasRead.tolower()
            
            #Runs while the user does not specifiy whether they have read the book or not
            while(hasRead!="true" or hasRead!="false"):
                hasRead = input("Have you read before?: ")
                hasRead = hasRead.tolower()
            
            read = bool(hasRead)
            userBook = Book(bookTitle, bookAuthor, year, read)
            userLibrary.addBook(userBook)
        elif userChoice==2:
            toRem = input("Enter the book title to remove: ")
            userLibrary.removeBook(toRem)
        elif userChoice==3:
            userLibrary.displayAll()
        elif userChoice==4:
            targetBook = input("Enter the book title to mark read: ")
            userLibrary.markBookRead(targetBook)
        elif userChoice==5:
            targetBook = input("Enter the book title to find: ")
            userLibrary.findBook(targetBook)
        elif userChoice==6:
            userLibrary.saveLibrary()
        else:
            userLibrary.loadLibrary()
        
if __name__ == "__main__":
    main() 
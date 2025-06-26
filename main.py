#JAM
#6/25/2025
#Acts as a personal library with several options for the user

from book import Book
from libraryManager import LibraryManager
from datetime import datetime

#Requests for the year the book was made
def requestYear():
    #Ensures that the input is a valid integer (not a float, String, etc)
    while True:
        bookYear = input("Enter the year the book was made: ")
        try:
            num = int(bookYear)
            
            #Ensures that input for book year is valid from 0-2025 (current year)
            if num<0 or num>datetime.now().year:
                print(f"Please enter a number between 0 and {datetime.now().year}\n")
            else:
                break
        except (ValueError, TypeError):
            print("Not valid book year\n")
    
    return num

#Requests if the user has read the book
def requestHasRead():
    didRead = input("Have you (read/unread) before?: ")
    didRead = didRead.lower()
    
    #Runs while the user does not specifiy whether they have read the book or not
    while(didRead!="read" and didRead!="unread"):
        didRead = input("Have you read before?: ")
        didRead = didRead.lower()
    
    #Determines whether they have read the book or not
    read = False
    if(didRead == "read"):
        read = True
        
    return read

def requestUserChoice():
    #Ensures that the input is a valid integer (not a float, String, etc)
    while True:
        userChoice = input("\nChoose an option: ")
        try:
            num = int(userChoice)
            
            #Ensures that input for book year is valid from 0-2025 (current year)
            if num<1 or num>10:
                print("Please enter a year between 1 and 10\n")
            else:
                break
        except (ValueError, TypeError):
            print("Not valid book year\n")
    
    return num
    
def libraryMenu():
    print("1. Add a new book")
    print("2. Remove a book")
    print("3. View all books")
    print("4. Sort books by year & title")
    print("5. Mark book read")
    print("6. Mark book unread")
    print("7. Search by Title")
    print("8. Save Library")
    print("9. Load Library")
    print("10. Exit")

def main():
    print("\nWelcome to Your Personal Library\n")
    userLibrary = LibraryManager()

    #Runs while the user decides not to exit (option 8)
    while True:
        libraryMenu()
        userChoice = requestUserChoice()
        
        #Quits early if the user decides to Exit
        if userChoice==10:
            print("Goodbye!")
            break
        
        #Acts accordingly based on the user's choice
        if userChoice==1:
            bookTitle = input("Enter the title of the book: ").strip()
            bookAuthor = input("Enter the author of the book: ")
            bookYear = requestYear()
            hasRead = requestHasRead()
            
            userBook = Book(bookTitle, bookAuthor, bookYear , hasRead)
            userLibrary.addBook(userBook)
        elif userChoice==2:
            toRem = input("Enter the book title to remove: ")
            userLibrary.removeBook(toRem)
        elif userChoice==3:
            userLibrary.displayAll()
        elif userChoice==4:
            userLibrary.sortBooks()
        elif userChoice==5:
            targetBook = input("Enter the book title to mark read: ")
            userLibrary.markBookRead(targetBook)
            print("\n")
        elif userChoice==6:
            targetBook = input("Enter the book title to mark unread: ")
            userLibrary.markBookUnread(targetBook)
            print("\n")
        elif userChoice==7:
            targetBook = input("Enter the book title to find: ")
            print(userLibrary.findBook(targetBook))
        elif userChoice==8:
            userLibrary.saveLibrary()
        else:
            userLibrary.loadLibrary()
        
if __name__ == "__main__":
    main() 
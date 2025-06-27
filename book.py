#JAM
#6/25/2025
#Stores a book and its information

class Book:
    def __init__(self,title, author, year, didRead):
        self.title = title
        self.author = author
        self.year = year
        self.didRead = didRead
    
    def toString(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Read: {self.didRead}\n"
    
    def getTitle(self):
        return self.title
    
    def getAuthor(self):
        return self.author
    
    def getYear(self):
        return self.year
    
    def getRead(self):
        return self.didRead
    
    #Marks the book read
    def markRead(self):
        self.didRead = True
    
    #Marks the book unread
    def markUnread(self):
        self.didRead = False

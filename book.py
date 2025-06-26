#JAM
#6/25/2025
#Stores a book and its information

class Book:
    def __init__(self,title, author, year, didRead):
        self.title = title
        self.author = author
        self.year = year
        self.didRead = didRead
    
    def __str__(self):
        return (f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Read: {self.didRead}\n")
    
    def getTitle(self):
        return self.title
    
    def getYear(self):
        return self.year
    
    #Marks the book read
    def markRead(self):
        self.didRead = True
    
    #Marks the book unread
    def markUnread(self):
        self.didRead = False
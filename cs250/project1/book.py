"""
Trevor Murphy
Project1 CS 250
February 2, 2015
FILE: book.py
Contains the Book class with methods:
readChar and readWord
"""

class Book:
    
    def __init__(self, filename):
        self.f = open(filename, "r")

    def readChar(self):
        #Reads a single character and returns it if it is an English letter
        letters = "qwertyuiopasdfghjklzxcvbnm"
        Letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
        ch = self.f.read(1)
        if ch in letters or ch in Letters:
            return ch
        return ""
    
    def readWord(self):
        #Uses readChar to build a word and return it
        ch = self.readChar()
        text = ""
        while ch != "":
            text += ch
            ch = self.readChar()
        return text

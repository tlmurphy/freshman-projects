"""
Trevor Murphy
Project1, CS 250
February 2, 2015
FILE: main.py
Contains the main function that opens a text file,
builds a wordlist, prints the max and min frequency
of words to output, then saves each word with
its corresponding frequency to two text files.
Result1 contains normal order, result2 contains
alphabetical order.

NOTE: Only works with python3
"""

import sys
from wordlist import *
from word import *
from book import *

def main():
    if len(sys.argv) != 2:
        print("Error: Need input file")
        return
    #According to my test of Les Miserables
    print("Finding words...takes about 6 minutes for 1000 pages of text")
    f = open(sys.argv[1], "r")
    length = len(f.read())
    f.close()

    wordList = WordList()
    book = Book(sys.argv[1])

    for i in range(0, length, 1):
        wordList.add(book.readWord())

    book.f.close()
    if length == 0:
        print("This is an empty file...")
        print("The highest frequency: None")
        print("The lowest frequency: None")
    else:
        print("The highest freqency:", wordList.maximum())
        print("The lowest frequency:", wordList.minimum())
    wordList.save("result1.txt")
    wordList.order()
    wordList.save("result2.txt")

main()

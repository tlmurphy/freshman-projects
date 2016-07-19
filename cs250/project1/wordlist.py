"""
Trevor Murphy
Project1, CS 250
February 2, 2015
FILE: wordlist.py
Contains the wordlist class with methods: add, order,
maximum, minimum, and save
"""
from word import *

class WordList:

    def __init__(self):
        #Create wordlist
        lyst = []
        self.__lyst = lyst

    def add(self, text):
        #method for adding text w/ freqency to wordlist
        if text == "":
            return

        for i in range(len(self.__lyst)):
            if text == self.__lyst[i].get_text():
                freq = self.__lyst[i].get_freq()
                freq += 1
                self.__lyst[i].set_freq(freq)
                return

        freq = 1
        word = Word(text, freq)
        self.__lyst.append(word)

    def order(self):
        #Sorst wordlist in alphabetical order
        self.__lyst = sorted(self.__lyst, key = lambda item: item.get_text())

    def maximum(self):
        #Return maximum freqency
        maxx = 0
        for i in range(len(self.__lyst)):
            if self.__lyst[i].get_freq() > maxx:
                maxx = self.__lyst[i].get_freq()
        return maxx

    def minimum(self):
        #Return minimum frequency
        minn = 10000000000000
        for i in range(len(self.__lyst)):
            if self.__lyst[i].get_freq() < minn:
                minn = self.__lyst[i].get_freq()
        return minn

    def save(self, filename):
        # Write contents of wordlist to an output file
        f = open('output_text/' + filename, "w")

        for i in range(len(self.__lyst)):
            f.write("%s:%d\n" % (self.__lyst[i].get_text(), self.__lyst[i].get_freq()))
        f.close()

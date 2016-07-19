""" 
Trevor Murphy
Project1, CS 250
February 2, 2015
FILE: word.py
Contains the word class with get and
set methods for text and frequency
of text
"""

class Word:
    def __init__(self, text, frequency):
        self.__text = text
        self.__freq = frequency

    def get_text(self):
        return self.__text
    def set_text(self, new_text):
        self.__text = new_text

    def get_freq(self):
        return self.__freq
    def set_freq(self, new_freq):
        self.__freq = new_freq

"""
Trevor Murphy
CS 250, Project 2
February 18, 2015
FILE: abstractbag.py

Contains the AbstractBag parent class
containing generalized methods for any
new bag classes that need to inherit
them
"""

class AbstractBag:
    def __init__(self, sourceCollection = None):
        self._size = 0
        #Able to add a collection to the bag
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def isEmpty(self):
        #Is the bag emtpy?
        return len(self) == 0

    def __len__(self):
        #Number of items in bag
        return self._size

    def __str__(self):
        #Prints the bag
        return "{" + ", ".join(map(str, self)) + "}"

    def __add__(self, other):
        #Add items to bag
        result = type(self)(self)
        for items in other:
            result.add(items)
        return result

    def __eq__(self, other):
        #Test for equality between bags
        if self is other: return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True

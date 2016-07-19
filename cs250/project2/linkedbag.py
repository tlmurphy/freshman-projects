"""
Trevor Murphy
CS 250, Project 2
Feb 18, 2015
FILE: abstractbag.py

Containst the AbstractBag class
with its necessary methods. Inherits
AbstractBag.
"""

from abstractbag import AbstractBag

class Node(object):
    #Need node class for linked list
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedBag(AbstractBag):
    def __init__(self, sourceCollection = None):
        self._items = None
        AbstractBag.__init__(self, sourceCollection)

    def __iter__(self):
        #Iterator for LinkedBag
        cursor = self._items
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next

    def clear(self):
        #Remove all items in linked bag
        self._size = 0
        self._items = None

    def add(self, item):
        #Add item to linked bag
        self._items = Node(item, self._items)
        self._size += 1

    def remove(self, item):
        #Remove an item from linked bag
        #Raises KeyError if item not in bag
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        self._size -= 1
        probe = self._items
        trailer = None
        for targetItem in self:
            if targetItem == item:
                break
            trailer = probe
            probe = probe.next
        if probe == self._items:
            self._items = self._items.next
        else:
            trailer.next = probe.next

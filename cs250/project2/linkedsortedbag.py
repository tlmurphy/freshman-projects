"""
Trevor Murphy
CS 250, Project 2
Feb 18, 2015
FILE: linkedsortedbag.py

Contains the LinkedSortedBag class with its
necessary methods. Inherits the LinkedBag 
class and its methods.
"""

from linkedbag import LinkedBag

class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedSortedBag(LinkedBag):
    def __init__(self, sourceCollection = None):
        LinkedBag.__init__(self, sourceCollection)

    def __contains__(self, item):
        #Does the linked bag contain this item?
        head = self._items
        probe = head
        while probe != None and item != probe.data:
            probe = probe.next
        if probe != None:
            return True
        else:
            return False

    def add(self, item):
        #Specialized add method for sorted linked bag
        self._size += 1
        probe = self._items
        
        #If nothing in bag
        if probe is None or probe.data > item:
            self._items = Node(item, self._items)
        
        #Else bag contains items
        else:
            while probe.next != None:
                if probe.next.data > item:
                    break
                probe = probe.next
            newNode = Node(item, probe.next)
            probe.next = newNode

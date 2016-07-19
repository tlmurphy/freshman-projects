"""
Trevor Murphy
CS 250, Project 2
Feb 18, 2015
FILE: main.py

Tests the classes and methods of abstractbag.py,
linkedbag.py, and linkedsortedbag.py
"""

from linkedbag import LinkedBag
from linkedsortedbag import LinkedSortedBag


def main():
    lyst = [6, 7, 8, 834, 43, 24, 86]

    #init
    b1 = LinkedBag(lyst)
    b2 = LinkedSortedBag(b1)

    #str
    print("Linked Bag:", b1)
    print("Sorted Linked Bag:", b2)

    #len
    print("Length of Linked Bag:", len(b1))
    print("Length of Sorted Linked Bag:", len(b2))

    #iter/contains
    print("Expect True:", 6 in b1)
    print("Expect False:", 785 in b2)
    print("Expect the items on separate lines:")
    for item in b1:
        print(item)

    #clear
    b1.clear()
    b2.clear()
    print("Linked Bag cleared:", b1)
    print("Sorted Linked Bag cleared:", b2)

    b1 = LinkedBag(lyst)
    b2 = LinkedSortedBag(b1)

    #eq
    print("Expect False:", b1 == b2)

    #add
    print("Expect two of each item:", b2 + b1)

    #remove
    for item in b1:
        b1.remove(item)
    for item in b2:
        b2.remove(item)
    print("Removed all items from Linked Bag:", b1)
    print("Removed all items from Sorted Linked Bag:", b2)

    #isEmpty
    print("Expect True:", b1.isEmpty())
    print("Expect True:", b2.isEmpty())

if __name__ == "__main__":
    main()

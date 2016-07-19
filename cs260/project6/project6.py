__author__ = 'Trevor'

"""
Trevor Murphy
CS 260 Project 6
April __, 2015
"""

import sys
from ArrayHeap import ArrayHeap


def main():
    array = [3, 2, 5, 6, 4, 345, 43, 21, 5, 77, 93]
    n = len(array)
    heap = ArrayHeap()
    for k in range(0, n):
        heap.add(array[k])
    print(heap._heap)


if __name__ == '__main__':
    main()

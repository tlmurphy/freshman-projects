"""
Trevor Murphy
FILE: swap.py
Contains the swap function to 
help out with sorting.
"""

def swap(lyst, i, j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

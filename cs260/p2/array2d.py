"""
Trevor Murphy
Lab 2, CS 250
February 2, 2015
FILE: array2d.py

Contains the Array2D class
"""
from swap import swap
import operator

class Array2D:
    def __init__(self, f):#, width, height):
        #Initialize the array
        grid = []
        width = 0
        height = 0

        grid = [s.split(",") for s in f.read().splitlines()]

        for rows in grid:
            height += 1
            for columns in rows:
                width += 1

        self._width = width // height
        self._height = height
        self.grid = grid

    def width(self):
        #Method for getting width
        return self._width

    def height(self):
        #Method for getting height
        return self._height

    def get_elem(self, row, col):
        #Returns an element at given coordinates
        return self.grid[row][col]

    def set_elem(self, row, col, element):
        #Assigns new element to given coordinates
        self.grid[row][col] = element

    def row(self, row_no):
        #Return list containing the elements in row
        return self.grid[row_no]

    def column(self, col_no):
        #Return list containing the elements in column
        lyst = []
        for h in range(self._height):
            lyst.append(self.grid[h][col_no])
        return lyst

    def __iter__(self):
        #Set up an iterator for the 2D array
        for h in range(self._height):
            for w in range(self._width):
                yield self.grid[h][w]

    def __len__(self):
        #How big is the 2D array? Note: Created for __eq__
        return self._width * self._height

    def __eq__(self, other):
        #Tests for equality
        if self is other: return True
        if type(self) != type(other): return False
        if len(self) != len(other): return False

        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True

    def __str__(self):
        #Allows the printing of the 2D array
        for r in range(self._height):
            for c in range(self._width):
                print(self.grid[r][c], end="\t")
            print()
        return ""

    def sorts(self, col_no, direction, types):
        #lyst = self.column(col_no)
        #lyst.remove(lyst[0]) #Remove header

        if direction == "descend":
            if types == "s":
                self.grid = sorted(self.grid, key = lambda x: str(x[col_no]))
            elif types == "f":
                self.grid = sorted(self.grid, key = lambda x: float(x[col_no]))
            else:
                self.grid = sorted(self.grid, key = lambda x: int(x[col_no]))
        else:
            if types == "s":
                self.grid = sorted(self.grid, key = lambda x: str(x[col_no]), reverse=True)
            elif types == "f":
                self.grid = sorted(self.grid, key = lambda x: float(x[col_no]), reverse=True)
            else:
                self.grid = sorted(self.grid, key = lambda x: int(x[col_no]), reverse=True)

        #return self.grid

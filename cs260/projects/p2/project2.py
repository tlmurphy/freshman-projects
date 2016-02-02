"""
Trevor Murphy
CS 260, Project 2
February 6, 2015

"""

import sys
from array2d import Array2D

def main():
    
    f = open(sys.argv[1], "r")
    g = open(sys.argv[2], "r")

    matrix1 = Array2D(f)
    matrix2 = Array2D(g)
    
    for row in matrix2.grid:
        if row[0] in matrix1.grid[0]:
            col_no = matrix1.grid[0].index(row[0])
            if row[1] == "ascend":
                if row[2] == "string":
                    matrix1.sorts(col_no, "ascend", "s")
                elif row[2] == "float":
                    matrix1.sorts(col_no, "ascend", "f")
                else:
                    matrix1.sorts(col_no, "ascend", "i")
            if row[1] == "descend":
                if row[2] == "string":
                    matrix1.sorts(col_no, "descend", "s")
                elif row[2] == "float":
                    matrix1.sorts(col_no, "descend", "f")
                else:
                    matrix1.sorts(col_no, "descend", "i")


    
    print(matrix1.grid)
    print(matrix1)
    #lystF2 = sorted(lystF2, key = lambda lystF2: lystF2[2])
    #print(lystF2)
    f.close()

main()


import os
import re
import sys
import numpy as np
def matric_package(inFile, outFile):
    f = open(inFile, "r")
    count = sum(1 for line in open('API-package.txt'))
    arr = []
    for line in f:
        arr.append(line)
    A = np.eye(count,dtype=int)
    # print(A)
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[x][arr[x].find(', L'):arr[x].find(';')] == arr[y][arr[y].find(', L'):arr[y].find(';')]:
                A[x][y] = 1
                # print(x, y)
    # print(A)
    for x in range(len(arr)):
        for y in range(len(arr)):
            outFile.write(str(A[x][y]) + "\t")
        outFile.write("\n")
pass
inFile = "API-package.txt"
resultFile = open("matric-package.txt", "w")

matric_package(inFile, resultFile)

resultFile.close()

print('done!')

import os
import re
import sys
import numpy as np
def matric_invoke(inFile, outFile):
    f = open(inFile, "r")
    count = sum(1 for line in open('read-line-smali-block.txt'))
    # print(count)
    arr = []
    for line in f:
        arr.append(line)
    A = np.eye(count,dtype=int)
    # print(A)
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[x][:arr[x].find('invoke')] == arr[y][:arr[y].find('invoke')]:
                A[x][y] = 1
    for x in range(len(arr)):
        for y in range(len(arr)):
            outFile.write(str(A[x][y]) + "\t")
        outFile.write("\n")
pass
inFile = 'read-line-smali-block.txt'
resultFile = open("matric-block.txt", "w")

matric_invoke(inFile, resultFile)

resultFile.close()

print('done!')

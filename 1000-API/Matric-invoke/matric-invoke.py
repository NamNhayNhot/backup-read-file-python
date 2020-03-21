import os
import re
import sys
import numpy as np
def matric_invoke(inFile, outFile):
    f = open(inFile, "r")
    count = sum(1 for line in open('API-invoke.txt'))
    arr = []
    for line in f:
        arr.append(line)
    A = np.eye(count)
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[x][0:12] == arr[y][0:12]:
                A[x][y] =1
    outFile.write(str(A))
    # print(A)

pass
inFile = "API-invoke.txt"
resultFile = open("matric-invoke.txt", "w")

matric_invoke(inFile, resultFile)

resultFile.close()

print('done!')

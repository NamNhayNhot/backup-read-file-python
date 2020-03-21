import os
import re
import sys
import numpy as np
def matric_package(inFile, outFile):
    api = open(inFile, "r")
    app = open("../Automatic reverse translation/Automatic-reverse-translation.txt", "r")
    count_api = sum(1 for line in open('API-app.txt'))
    count_app = sum(1 for line in open('../Automatic reverse translation/Automatic-reverse-translation.txt'))
    arr_api = []
    for line_api in api:
        arr_api.append(line_api)
    # print(len(arr_api))
    arr_app = []
    for line_app in app:
        arr_app.append(line_app.strip())
    # print(len(arr_app))
    A = np.zeros( (count_api, count_app) )
    for x in range(len(arr_api)):
        for y in range(len(arr_app)):
            if arr_api[x][2:arr_api[x].find('    invoke')] == arr_app[y]:
                A[x][y] = 1
                # print(arr_api[x][2:arr_api[x].find('invoke')])
                # print(arr_app[y])
                # print(x, y)
    # print(A)
    outFile.write(str(A))
pass
inFile = "API-app.txt"
resultFile = open("matric-app.txt", "w")

matric_package(inFile, resultFile)

resultFile.close()

print('done!')

print()
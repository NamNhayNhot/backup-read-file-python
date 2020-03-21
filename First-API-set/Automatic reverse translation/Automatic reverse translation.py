import os
import numpy as np

def readFileFolder(inFile, outFile):
    f = open(inFile, "r")
    for x in f:
        if x[len(x)-2] == "/":
            outFile.write(str(x[:len(x)-2])+'\n')
pass
inFile = "/home/dieuthuy/Khoa-luan-tot-nghiep/dich-nguoc/dich-tu-dong.txt"
resultFile = open("Automatic-reverse-translation.txt", "w")

readFileFolder(inFile, resultFile)

resultFile.close()

print('done!')
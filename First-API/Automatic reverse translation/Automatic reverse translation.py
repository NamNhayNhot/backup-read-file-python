import os
import numpy as np

def readFileFolder(inFile, outFile):
    f = open(inFile, "r")
    for x in f:
        if x[len(x)-2] == "/":
            outFile.write(str(x[:len(x)-2])+'\n')
pass
inFile = "/home/dieuthuy/khoaluantotnghiep/samples-20200311T150501Z-001/samples/malware/malware_samples/dich-tu-dong.txt"
resultFile = open("Automatic-reverse-translation.txt", "w")

readFileFolder(inFile, resultFile)

resultFile.close()

print('done!')
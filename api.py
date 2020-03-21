import os
import numpy as np

def readFileSmali(inFile, outFile):
    f = open(inFile, "r")
    thisset = {""}
    for x in f:
        thisset.add(x)
    for letter in set(thisset):
        outFile.write(letter)

pass
inFile = "list-api-coincide.txt"
resultFile = open("api.txt", "w")

readFileSmali(inFile, resultFile)

resultFile.close()

print('done!')

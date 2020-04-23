def readFileFolder(inFile, outFile):
    if inFile == "/home/dieuthuy/khoaluantotnghiep/malware/malware_samples/dich-tu-dong.txt" :
        f = open(inFile, "r")
        for x in f:
            if x[len(x) - 2] == "/":
                outFile.write(str('1 - ' + x[:len(x) - 2]) + '\n')
    else:
        f = open(inFile, "r")
        for x in f:
            if x[len(x) - 2] == "/":
                outFile.write(str('0 - ' + x[:len(x) - 2]) + '\n')


pass
arr = ["malware/malware_samples", "benign/benign_samples"]
resultFile = open("Automatic-reverse-translation.txt", "w")
inFile = ""
for i in arr:
    inFile = "/home/dieuthuy/khoaluantotnghiep/"+i+"/dich-tu-dong.txt"
    readFileFolder(inFile, resultFile)

resultFile.close()

print('done!')
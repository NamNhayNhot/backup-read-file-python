import os
def readAllFile(currentPath, outFile):
    fileList = os.listdir(currentPath)
    for name in fileList:
        fileName = currentPath + "/" + name
        if (os.path.isfile(fileName)):
            if ".smali" in fileName:
                f = open(fileName, "r")
                fileContent = f.readlines()
                # outFile.write("\n------>" + fileName+": \n")
                for x in fileContent:
                   if x.find('.method') != -1 or x.find('    invoke') != -1 or x.find('.end method') != -1:
                       outFile.write(x)
        else:
            if (os.path.isdir(fileName)):
                readAllFile(fileName, outFile)
pass
resultFile = open("API-first-method-endMethod.txt", "w")
automatic = open("Automatic reverse translation/Automatic-reverse-translation.txt", "r")
path = ""
for line in automatic:
    path ="/home/dieuthuy/Khoa-luan-tot-nghiep/dich-nguoc/"+line.strip()+"/smali"
    readAllFile(path, resultFile)
resultFile.close()
print('done!')
import os
thisset = set()
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
                   if "    invoke" in x:
                       if x not in thisset:
                        thisset.add(x)
        else:
            if (os.path.isdir(fileName)):
                readAllFile(fileName, outFile)
pass
resultFile = open("API-first-set.txt", "w")
automatic = open("3000-API/Automatic reverse translation/Automatic-reverse-translation.txt", "r")
path = ""
for line in automatic:
    path ="/home/dieuthuy/Khoa-luan-tot-nghiep/dich-nguoc/"+line.strip()+"/smali"
    readAllFile(path, resultFile)
for letter in thisset:
    resultFile.write(letter)
resultFile.close()
print('done!')



# import os
# def readAllFile(currentPath, outFile):
#     fileList = os.listdir(currentPath)
#     for name in fileList:
#         fileName = currentPath + "/" + name
#         if (os.path.isfile(fileName)):
#             if ".smali" in fileName:
#                 f = open(fileName, "r")
#                 fileContent = f.readlines()
#                 outFile.write("\n------>" + fileName+": \n")
#                 thisset = set()
#                 for x in fileContent:
#                    if '    invoke' in x:
#                        # outFile.write(x)
#                        thisset.add(x.strip())
#                         # outFile.write(x)
#                 # outFile.write(str(thisset))
#                 # print(thisset)
#                 for letter in set(thisset):
#                     outFile.write(letter + "\n")
#                     # print(letter)
#                         # outFile.write(x)
#                         # print(x)
#                 # print(fileContent)
#         else:
#             if (os.path.isdir(fileName)):
#                 readAllFile(fileName, outFile)
# pass
#
# resultFile = open("API-first-set.txt", "w")
#
# readAllFile("/home/dieuthuy/Khoa-luan-tot-nghiep/dich-nguoc/Stick/smali", resultFile)
#
# resultFile.close()
#
# print('done!')




# import os
# def readAllFile(currentPath, outFile):
#     fileList = os.listdir(currentPath)
#     for name in fileList:
#         fileName = currentPath + "/" + name
#         if (os.path.isfile(fileName)):
#             if ".smali" in fileName:
#                 f = open(fileName, "r")
#                 fileContent = f.read()
#                 outFile.write("\n------>" + fileName+": \n")
#                 outFile.write(fileContent)
#         else:
#             if (os.path.isdir(fileName)):
#                 readAllFile(fileName,outFile)
# pass
#
#
# resultFile = open("API-first-set.txt", "w")
#
# readAllFile("/home/dieuthuy/Khoa-luan-tot-nghiep/dich-nguoc/Stick/smali",resultFile)
#
# resultFile.close()
#
# print('done!')

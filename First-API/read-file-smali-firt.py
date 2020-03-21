import os
def readAllFile(currentPath, outFile):
    fileList = os.listdir(currentPath)
    for name in fileList:
        fileName = currentPath + "/" + name
        if (os.path.isfile(fileName)):
            if ".smali" in fileName:
                f = open(fileName, "r")
                fileContent = f.readlines()
                outFile.write("\n------>" + fileName+": \n")
                for x in fileContent:
                   if "    invoke" in x:
                       outFile.write(x)
        else:
            if (os.path.isdir(fileName)):
                readAllFile(fileName, outFile)
pass
resultFile = open("API-first.txt", "w")
automatic = open("Automatic reverse translation/Automatic-reverse-translation.txt", "r")
path = ""
for line in automatic:
    path ="/home/dieuthuy/khoaluantotnghiep/samples-20200311T150501Z-001/samples/malware/malware_samples/"+line.strip()+"/smali"
    readAllFile(path, resultFile)
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

import os
# thisset = set()
arr = []
def readAllFile(currentPath, outFile):
    fileList = os.listdir(currentPath)
    for name in fileList:
        fileName = currentPath + "/" + name
        if (os.path.isfile(fileName)):
            if ".smali" in fileName:
                f = open(fileName, "r")
                fileContent = f.readlines()
                for x in fileContent:
                    if x.find('.method') != -1 or x.find('    invoke') != -1:
                       arr.append(x)
        else:
            if (os.path.isdir(fileName)):
                readAllFile(fileName, outFile)
pass

resultFile = open("read-line-smali-block.txt", "w")
automatic = open("../../1000-API/Automatic reverse translation/Automatic-reverse-translation.txt", "r")
path = ""
for line in automatic:
    path ="/home/dieuthuy/khoaluantotnghiep/malware/malware_samples/"+line.strip()+"/smali"
    readAllFile(path, resultFile)
# resultFile.close()
arr_new = []
i = ''
for x in range(-1,len(arr)):
    if arr[x].find('.method') != -1:
        i = arr[x]
        continue
    arr_new.append(i.strip() + arr[x])
#     resultFile.write(i.strip() + arr[x])
# resultFile.close()
# api_block = open("API-block.txt")
# open_read_line_smali = open('read-line-smali-block.txt','r')

# for line in open_read_line_smali:
#     arr_new.append(line)
    # arr_new.append(i.strip() + arr[x])
# print(arr_new)
# for i in arr_new:
#     print(i)


def pr_N_mostFrequentNumber(arr_new, n, k):
    global resultFile
    um = {}
    for i in range(n):
        if arr[i] in um:
            um[arr_new[i]] += 1
        else:
            um[arr_new[i]] = 1
    a = [0] * (len(um))
    j = 0
    for i in um:
        a[j] = [i, um[i]]
        j += 1
    a = sorted(a, key=lambda x: x[0], reverse=True)
    a = sorted(a, key=lambda x: x[1], reverse=True)

    # display the top k numbers
    print(k, "numbers with most occurrences are:")
    for i in range(k):
        resultFile.write(a[i][0])
        # print(a[i][0])
if __name__ == "__main__":
    n = len(arr_new)
    k = 1000
    pr_N_mostFrequentNumber(arr_new, n, k)
# for letter in arr:
#     # print(letter)
#     resultFile.write(letter)
resultFile.close()
print('done!')






# import os
# thisset = set()
# def readAllFile(currentPath, outFile):
#     fileList = os.listdir(currentPath)
#     for name in fileList:
#         fileName = currentPath + "/" + name
#         if (os.path.isfile(fileName)):
#             if ".smali" in fileName:
#                 f = open(fileName, "r")
#                 fileContent = f.readlines()
#                 for x in fileContent:
#                     if x.find('.method') != -1 or x.find('    invoke') != -1:
#                         if x not in thisset:
#                             thisset.add(x)
#                             # thisset.add(x[x.find("L"):x.find("(")] + "\n")
#         else:
#             if (os.path.isdir(fileName)):
#                 readAllFile(fileName, outFile)
#
#
# pass
# resultFile = open("read-line-smali-block.txt", "w")
# automatic = open("../Automatic reverse translation/Automatic-reverse-translation.txt", "r")
# path = ""
# for line in automatic:
#     path = "/home/dieuthuy/Khoa-luan-tot-nghiep/dich-nguoc/" + line.strip() + "/smali"
#     readAllFile(path, resultFile)
# for letter in thisset:
#     resultFile.write(letter)
# resultFile.close()
# read_file_block = open('read-line-smali-block.txt', 'r+')
# count = sum(1 for line in open('read-line-smali-block.txt'))
# arr = []
# for line in read_file_block:
#     arr.append(line)
# # print(arr)
# i = ''
# api_block= open('API-block.txt', 'w')
# for x in range(-1,len(arr)):
#     if arr[x].find('.method') != -1:
#         i = arr[x]
#         continue
#     # print(i.strip() +"0"+ arr[x])
#     api_block.write(i.strip() + arr[x])
# print('done!')

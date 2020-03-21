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
                # outFile.write("\n------>" + fileName+": \n")
                for x in fileContent:
                   if "    invoke"  in x:
                       # if x not in thisset:
                       arr.append(x)
                       # arr.append(fileName[fileName.find('c/'):fileName.find('/smali')] + x)
                       # arr.append(x[x.find("L"):x.find("(")] + "\n")
                        # thisset.add(x[x.find("L"):x.find("(")] + "\n")
                        # thisset.add(x[x.find("->"):x.find("(")] + "\n")
        else:
            if (os.path.isdir(fileName)):
                readAllFile(fileName, outFile)
pass

resultFile = open("API-request.txt", "w")
automatic = open("3000-API/Automatic reverse translation/Automatic-reverse-translation.txt", "r")
path = ""
for line in automatic:
    path ="/home/dieuthuy/Khoa-luan-tot-nghiep/dich-nguoc/"+line.strip()+"/smali"
    readAllFile(path, resultFile)


def pr_N_mostFrequentNumber(arr, n, k):
    global resultFile
    um = {}
    for i in range(n):
        if arr[i] in um:
            um[arr[i]] += 1
        else:
            um[arr[i]] = 1
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

    # Driver code


if __name__ == "__main__":
    n = len(arr)
    k = 1000
    pr_N_mostFrequentNumber(arr, n, k)
# for letter in arr:
#     # print(letter)
#     resultFile.write(letter)
resultFile.close()
print('done!')
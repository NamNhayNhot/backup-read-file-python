import numpy as np
def matric_package(inFile, outFile):
    api = open(inFile, "r")
    app = open("../Automatic reverse translation/Automatic-reverse-translation.txt", "r")
    count_api = sum(1 for line in open('API-app.txt'))
    count_app = sum(1 for line in open('../Automatic reverse translation/Automatic-reverse-translation.txt'))
    arr_api = []
    for line_api in api:
        arr_api.append(line_api)
    arr_app = []
    for line_app in app:
        arr_app.append(line_app.strip())
    A = np.zeros((count_api, count_app),dtype=int )
    for x in range(len(arr_api)):
        for y in range(len(arr_app)):
            if arr_api[x][2:arr_api[x].find('    invoke')] == arr_app[y]:
                A[x][y] = 1
    for x in range(len(arr_api)):
        for y in range(len(arr_app)):
            outFile.write (str(A[x][y])+"\t")
        outFile.write("\n")
pass
inFile = "API-app.txt"
resultFile = open("matric-app.txt", "w")
matric_package(inFile, resultFile)
resultFile.close()
print('done!')

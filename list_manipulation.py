def readName(data):
    with open("names.csv") as file:
        data.append(file.read().strip('\n'))

def loadMatrix(data,mat):
    mat.extend(data[0].strip().split('\n'))
    print("load matrix:",mat)

def convertToColumnMajor(mat):
    temp = []
    n = max([len(i) for i in mat])
    for i in range(n):
        res = ""
        for j in range(len(mat)):
            try:
                res += mat[j][i]

            except Exception as e:
                res += " "
        temp.append(res.rstrip().lstrip())
    mat.clear()
    mat.extend(temp)
    print("Column major:",mat)

def calculateCharacterLength(mat):
    res = 0
    for i in mat:
        res += len(i.replace(" ",""))
    print("Character length: ",res)

def storeListAsString(mat):
    #convertToColumnMajor(mat)
    with open("output.txt","wt") as file:
        for i in mat:
            file.write(i)

def main():
    data = []
    mat = []
    readName(data) #done
    loadMatrix(data,mat) #done
    convertToColumnMajor(mat) #done
    calculateCharacterLength(mat) #done
    storeListAsString(mat) #done

main()
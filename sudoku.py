array =[]

for i in range(9):
    temp = list(map(int, input().split()))  
    array.append(temp)

def checkRow(array):
    for temp in array:
        for i in range(9):
            for j in range(i+1,9):
                if temp[i] == temp[j]:
                    return False
    return True

def checkCol(array):
    for i in range(9):
        for j in range(9):
            for k in range(j+1,9):
                if array[j][i] == array[k][i]:
                    return False
    return True

def checkThreeBoard(array):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [array[row][col] for row in range(i, i+3) for col in range(j, j+3)]
            for k in range(9):
                for l in range(k+1, 9):
                    if subgrid[k] == subgrid[l]:
                        return False
    return True

if (checkRow(array) and checkCol(array) and checkThreeBoard(array)):
    print("YES")
else:
    print("NO")
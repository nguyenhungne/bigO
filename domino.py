def dominoCount(n):
    if n == 0:
        return 0
    temp = 0

    array = []
    for i in range(n):
        array.append(int(input()))

    count = 1

    for i in range(n - 1):
        if array[i] == array[i + 1]:
            count += 1
            if count >= 2:
                temp += 1
        else:
            count = 1
        

    return temp

n = int(input())
print(dominoCount(n))
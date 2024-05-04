m, k = map(int, input().split())

array = []
for i in range(m):
    temp = list(map(float, input().split()))
    array.append(temp)

array.sort(key=lambda x: (-x[1], x[0]))

for i in range(k):
    print(int(array[i][0]))

import sys
sys.setrecursionlimit(10000000)

def sort_array(array):
    even_positions = []
    for i in array:
        if i % 2 == 0:
            even_positions.append(i)

    odd_positions = []
    for i in array:
        if i % 2 != 0:
            odd_positions.append(i)
    even_positions.sort()
    odd_positions.sort(reverse=True)
    result = []
    for i in array:
        if i % 2 == 0:
            result.append(even_positions.pop(0))
        else:
            result.append(odd_positions.pop(0))
    return result


n = int(input())
array = list(map(int, input().split()))
array = sort_array(array)

for item in array:
    print(item, end=' ')
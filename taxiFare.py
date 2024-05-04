n = int(input())

result = 0
if n <= 0:
    result = 0
elif n <= 1:
    result += n*15000
elif n <= 5:
    result += 1*15000 + (n-1)*13500
elif n < 12:
    result += 1*15000 + 4*13500 + (n-5)*11000
else:
    result += (1*15000 + 4*13500 + 7*11000 + (n-12)*11000)*0.9

print(round(result))
from math import log

num = int(input().strip())
base = int(input().strip())

if base < 0 or base in [0, 1]:
    result = log(num)
else:
    result = log(num, base)

print(round(result, 2))

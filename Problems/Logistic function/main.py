from math import exp

v = float(input())

result = exp(v) / (exp(v) + 1)

print(round(result, 2))

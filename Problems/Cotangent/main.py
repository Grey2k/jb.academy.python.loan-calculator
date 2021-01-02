from math import tan, radians

angle = int(input().strip())

cotangent = 1 / tan(radians(angle))

print(round(cotangent, 10))

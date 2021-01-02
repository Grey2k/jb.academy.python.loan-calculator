from math import sqrt

edge = int(input().strip())

area = 2 * sqrt(3) * pow(edge, 2)
volume = 1 / 3 * sqrt(2) * pow(edge, 3)

print("{} {}".format(round(area, 2), round(volume, 2)))

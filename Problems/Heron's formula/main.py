# put your python code here
from math import sqrt

a = float(input().strip())
b = float(input().strip())
c = float(input().strip())


def half_perimeter(a_side: float, b_side: float, c_side: float) -> float:
    return (a_side + b_side + c_side) / 2


p = half_perimeter(a, b, c)

result = sqrt(p * (p - a) * (p - b) * (p - c))

print(result)

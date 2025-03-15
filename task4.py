from math import sqrt


def distance(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)

    return sqrt(width ** 2 + height ** 2)

print(distance(0, 0, 5, 0))
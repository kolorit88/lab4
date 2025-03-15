def triangle(a, b, c):

    args = sorted([a, b, c])
    if args[-1] < args[0] + args[1]:
        print("Это треугольник")
        return
    print("Это не треугольник")

triangle(1, 2, 4)
triangle(2, 3, 4)

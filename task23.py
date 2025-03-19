def matrix(n=None, m=None, a=0):
    matrix = []
    if n is None:
        n = 1
    if m is None:
         m = n

    for _ in range(n):
        matrix.append([a for _ in range(m)])

    return matrix

rows = matrix()
print(*rows, sep='\n')
rows = matrix(2)
print(*rows, sep='\n')
rows = matrix(4, 3, 1)
print(*rows, sep='\n')
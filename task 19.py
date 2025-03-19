def transpose(matrix):
    copy = matrix.copy()
    matrix.clear()
    matrix.extend(list(zip(*copy)))

m = [[1, 2], [3, 4]]
transpose(m)
print(m)
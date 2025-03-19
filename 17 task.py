def mirror(arr):
    arr.extend(arr[::-1])
    return arr

print(mirror([1, 2, 3]))


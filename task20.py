def swap(first, second):
    container = first[:]
    first.clear()
    first.extend(second[:])
    second.clear()
    second.extend(container)


first = [1, 2]
second = [3, 4]
swap(first, second)
print(first, second)
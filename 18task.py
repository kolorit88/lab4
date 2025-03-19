def from_string_to_list(string, container):
    container.extend(map(lambda x: int(x), string.split(' ')))

a = [1, 2, 3]
from_string_to_list("33 44 55", a)
print(a)

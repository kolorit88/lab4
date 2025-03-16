print("Неправильный вариант: не работает, т.к списки odd и even ссылаются на один объект")
# Программа разделяет числа из списка numbers на два списка odd и even (чет. и нечет. числа)

numbers = [2, 5, 7, 7, 8, 4, 1, 6]
odd = even = []

for number in numbers:
 if number % 2 == 0:
    even.append(number)
 else:
    odd.append(number)

print(odd, even)
print("Исправленный вариант, где odd и even - разные списки:")

numbers = [2, 5, 7, 7, 8, 4, 1, 6]
odd = []
even = []

for number in numbers:
 if number % 2 == 0:
    even.append(number)
 else:
    odd.append(number)

print(odd, even)
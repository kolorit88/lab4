# Исходный список
original_list = [5, 4, 3, 2, 1]
print("Исходный список:", original_list)

original_list.sort()
print("Исходный список после sort()", original_list)

original_list = [5, 4, 3, 2, 1]
print("Обновили исходный список:", original_list)

sorted(original_list)
print("Исходный список после sorted()", original_list)

# sort изменяет список и ничего не возвращает
# sorted не изменяет оригинальный список, а возвращает новый отсортированный

value = [1, 2, 3]
addition = [4, 5]

print("ID до операции:", id(value))  # ID до операции

# Используем value = value + addition
value = value + addition
print("ID после value = value + addition:", id(value))  # ID изменился

# Сбрасываем значение
value = [1, 2, 3]

print("ID до операции:", id(value))  # ID до операции

# Используем value += addition
value += addition
print("ID после value += addition:", id(value))  # ID остался тот же
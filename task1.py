my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 18, 20, 66]

new_list_1 = list(filter(lambda x: x < 5, my_list))
print(new_list_1)

new_list_2 = list(map(lambda x: x / 2, my_list))
print(new_list_2)

new_list_3 = list(filter(lambda x: x * 2 > 17, my_list))
print(new_list_3)
new_list_3 = list(map(lambda x: x * 2, filter(lambda x: x > 17, my_list)))
print(new_list_3)

new_list_4 = [i ** 2 for i in range(int(input("введите число")) + 1)]
print(new_list_4)

new_list_5 = [int(elem) ** 2 for elem in
        input("введите последовательность число").split()]
print(new_list_5)

new_list_6 = [int(elem) ** 2 for elem in input("введите последовательность число").split()
              if str(int(elem) ** 2)[-1] != "9" and int(elem) % 2 != 0]
print(new_list_6)



friends_dict = dict()

def add_friends(name, list_of_friends):
    global friends_dict

    if name not in friends_dict:
        friends_dict[name] = list_of_friends
    else:
        friends_dict[name].extend(list_of_friends)

    for friend_name in list_of_friends:
        if friend_name not in friends_dict:
            friends_dict[friend_name] = [name]
        else:
            friends_dict[friend_name].append(name)


def are_friends(name, second_name):
    global friends_dict

    if name not in friends_dict:
        return False
    return second_name in friends_dict[name]

def print_friends(name):
    global friends_dict
    if name in friends_dict:
        print(" ".join(sorted(friends_dict[name])))


add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))

print_friends("Алла")
print_friends("Мария")
print_friends("Иван")
print_friends("Марина")
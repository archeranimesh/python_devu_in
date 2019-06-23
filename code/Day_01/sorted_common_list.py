# WAP to find common elements in 2 list.

my_list_1 = [1, 2, 3, 4]
my_list_2 = [4, 6, 7, 8]

print("list Comprehension: ", [x for x in my_list_1 if x in my_list_2])


def common_list_2(list_1, list_2):
    return_list = []
    for x in list_1:
        if x in list_2:
            return_list.append(x)
            print(return_list)
    return sorted(return_list)


def common_list(list_1, list_2):
    retun_list = []
    for x in list_1:
        for y in list_2:
            if x == y:
                retun_list.append(x)
    return sorted(retun_list)


print(common_list(my_list_1, my_list_2))
print(common_list_2(my_list_1, my_list_2))


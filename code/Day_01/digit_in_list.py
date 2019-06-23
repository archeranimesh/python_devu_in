my_list = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]
find_no = 1


def count_number(my_list, find_no):
    return str(my_list).count(str(find_no))


print(count_number(my_list, find_no))


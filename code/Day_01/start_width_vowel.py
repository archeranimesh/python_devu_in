# WAP to find the list of domain name starting with vowels.
domain_name = ["Apple", "Google", "Microsoft", "igate", "oracle", "devu"]

print("list comprehension: ", [x for x in domain_name if x[0].lower() in "aeiou"])


def find_vowel_0_index(domain_name):
    return_list = []
    for x in domain_name:
        # print(x, x[0])
        if x[0].lower() in "aeiou":
            return_list.append(x)
    return return_list


print(find_vowel_0_index(domain_name))

# WAP to reverse the key:value pair of dict.
d = {1: 10, 2: 20, 3: 30}

names = {1: "Amit", 2: "Baju", 3: "Chandu"}

names_1 = {1: "Amit", 2: "Baju", 3: "Chandu", 4: "Amit"}

c = {v: k for k, v in names.items()}

w = {v: [i for i in names_1.keys() if names_1[i] == v] for k, v in names_1.items()}

print(c)
print(w)


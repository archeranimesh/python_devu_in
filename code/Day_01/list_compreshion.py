# should end in list
a = [1, 2, 3, 4, 5]
b = [x ** 2 for x in a]  # Map
c = [x for x in a if x > 3]  # filter
d = [x ** 2 for x in a if x > 3]  # Map + Filter

print("Original List", a)
print("Square Map: ", b)
print("Filter for x > 3: ", c)
print("Map/Filter :", d)


word = "Apple"
print("Only Vowel in word: : ", [x for x in word if x.lower() in "aeiou"])

data = ["Yes", "NO", "yes", "YES", "", "no"]
# ternary operator
print(
    "Ternary operator with map/filter: ", [1 if i.lower() == "yes" else 0 for i in data]
)

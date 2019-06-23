# WAP to get a dict of letters and their count from a given word.
# "apple" - {}

myString = "apple"
myDict = {x: myString.count(x) for x in myString}
print(myDict)

# WAP data compression for sparse vector
a = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2]
myNewDict = {x: a[x] for x in range(len(a)) if a[x] > 0}
print(myNewDict)

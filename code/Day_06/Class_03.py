import sys

list_a = [1, 2, 3, 4, 5, 6, 7, 8]
iter_a = iter(list_a)

try:
    while True:
        print(next(iter_a))
except StopIteration as identifier:
    pass

list_b = [i for i in range(10000)]
list_c = iter(range(10000))

print("Size of a is % bytes", sys.getsizeof(list_b))
print("Size of b is % bytes", sys.getsizeof(list_c))

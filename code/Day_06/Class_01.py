def generator_function(num):
    i = 0
    while i < num:
        print("i = ", i)
        i += 1


# Original Generator
def my_generator_function(num):
    i = 0
    while i < num:
        yield i
        i += 1


if __name__ == "__main__":
    print(generator_function(4))
    x = my_generator_function(4)

    try:
        while True:
            print(next(x))
    except StopIteration as si:
        print("iteration ended with: ")


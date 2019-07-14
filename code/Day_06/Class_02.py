# Generator expression

a = [1, 2, 3]
b = (i ** 2 for i in a)


if __name__ == "__main__":

    try:
        while True:
            print(next(b))
    except StopIteration as si:
        print("loop ended")

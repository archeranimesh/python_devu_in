# Threads

import time, threading


def square(x):
    for i in x:
        time.sleep(0.5)
        print("square: ", i ** 2)


def cube(x):
    for i in x:
        time.sleep(0.4)
        print("Cube: ", i ** 3)


if __name__ == "__main__":
    x = [1, 2, 4, 234, 2345]
    thread1 = threading.Thread(target=square, args=(x,))
    thread2 = threading.Thread(target=cube, args=(x,))

    thread1.start()
    thread2.start()


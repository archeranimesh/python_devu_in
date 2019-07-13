# Operator Overloading
# vector addition.


class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y


if __name__ == "__main__":
    obj1 = A(2, 3)
    obj2 = A(4, 5)
    print(obj1 + obj2)

class A:
    def __init__(self, x, y):
        # instance variable
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y


if __name__ == "__main__":
    objA = A(12, 15)
    print(objA.add())
    print(objA.sub())

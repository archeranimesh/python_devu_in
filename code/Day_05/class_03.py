class A:
    x = 1000  # static

    def add(self, c):
        return self.x + c


if __name__ == "__main__":
    objA = A()
    print(objA.add(100))

    objB = A()
    print(objB.add(300))


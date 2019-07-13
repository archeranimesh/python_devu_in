class A:
    def greetings(self):
        return "Hello from A"


class B:
    def greetings(self):
        return "Hello from B"


class C(B, A):  # L-R priority
    pass


class D(A, B):  # L-R priority
    pass


if __name__ == "__main__":
    objC = C()
    print(objC.greetings())

    objD = D()
    print(objD.greetings())

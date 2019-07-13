class A:
    def greetings(self):
        return "Hello from A"


class B(A):
    def greetings(self):
        return "Hello from B"


class C(B):
    pass


if __name__ == "__main__":
    objC = C()
    print(objC.greetings())  # Nearest parent

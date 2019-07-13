class A:
    def greetings(self):
        return "Hello from A"


class B(A):
    def greetings(self):
        return "Hello from B"


# TypeError: Cannot create a consistent method resolution
class C(A, B):
    pass


if __name__ == "__main__":
    objC = C()
    print(objC.greetings())

# Multi Level Inheritance
class A:
    value = 123

    def greetings(self):
        return "hello, world"


class B(A):
    pass


class C(B):
    pass


if __name__ == "__main__":
    objC = C()
    print(objC.value)
    print(objC.greetings())

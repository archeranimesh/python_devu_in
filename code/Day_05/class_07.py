# Multiple Inheritance
class A:
    value = 123

    def greetings(self):
        return "hello, world"


class B:
    def greet_local(self):
        return "Namaste"


# Multiple Inheritance
class C(A, B):
    pass


if __name__ == "__main__":
    objC = C()
    print(objC.value)
    print(objC.greet_local())
    print(objC.greetings())

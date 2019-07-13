class A:
    value = 123

    def greetings(self):
        return "hello, world"


# Single Inheritance
# Share all attributes from base class A
class B(A):
    pass


if __name__ == "__main__":
    objA = A()
    print(objA.value)
    print(objA.greetings())

    objB = B()
    print(objB.value)
    print(objB.greetings())

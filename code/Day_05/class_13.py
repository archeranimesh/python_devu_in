# Pseudo Private Variable.


class A:
    __x = 123

    def __greetings(self):
        return "hello"

    def __str__(self):
        return "It is the object of class A"


if __name__ == "__main__":
    objA = A()
    # AttributeError: 'A' object has no attribute '__x'
    # print(objA.__x)
    # access the private variable with _ClassName__variable
    print(objA._A__x)
    # Class  the overridden __str__ function
    print(objA)

# Over-riding
class A:
    def greetings(self):
        return "Hello from A"


class B(A):
    def greetings(self):
        return "Hello from B"


if __name__ == "__main__":
    objB = B()
    print(objB.greetings())

def NEWUSER100(fxn):
    def wrapper(amt):
        return fxn(amt) - 100

    return wrapper


def HDFC50(fxn):
    def wrapper(amt):
        return fxn(amt) - 50

    return wrapper


@HDFC50
@NEWUSER100
def billing(amount):
    return amount


print(billing(1000))

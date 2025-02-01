# Class based deccorators
class Test:
    @classmethod
    def dec(cls, func):
        def wrapper(arg):
            print("Before")
            func(arg)
            print("After")
        return wrapper


@Test.dec
def f(s):
    print(s)


f("test")


# Function based deccorators
def decc(func):
    def wrapper(arg):
        print("Before")
        func(arg)
        print("After")
    return wrapper


@decc
def ff(s):
    print(s)


ff("test2")

"""
    Implementing the decorator design pattern in python using closures.
"""


def dec(f):
    def wrapper():
        print("...")
        f()
        print("...")
    return wrapper


@dec
def func():
    print("Andrei")


func()

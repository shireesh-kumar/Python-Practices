# Decorators
import functools


def startAndStopTimmer(func):
    @functools.wraps(func)  # keeps the actual name of the function
    def wrapper(*args, **kwargs):
        print("start")
        func(*args, **kwargs)
        print("end")
    return wrapper


# def func():
#     print("timmer started ")

# #non decorator method
# func = startAndStopTimmer(func)
# func()


# Decorator Method
@startAndStopTimmer
def func1(x,y,z):
    print(x + y + 5)
    print(z[1])


func1(3,7,[{'a','b'},{'c':1}])

# interpretor basically get confused by the name of the function so we use a external decorator
#print(func1.__name__)

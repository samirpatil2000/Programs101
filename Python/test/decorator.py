
def to_lowercase(function):
    def wrapper(arg):
        func = function(arg)
        return func.lower()
    return wrapper

def to_highercase(function):
    def wrapper(arg):
        arg += arg
        func = function(arg)
        return func.upper()
    return wrapper
# 
@to_lowercase
@to_highercase

def hello(arg):
    return "Hello world!" + arg

print(hello("Samir"))

print([i for i in range(20) if i % 2 == 0])
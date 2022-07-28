# decorator function to convert to lowercase


def lowercase_decorator(function):
    def wrapper(*args, **kwargs):
        print("hello lowercase_decorator")
        result = function(*args, **kwargs)
        string_lowercase = result.lower()
        return string_lowercase
    return wrapper

# decorator function to split words
def splitter_decorator(function):
    def wrapper(*args, **kwargs):
        print("hello splitter_decorator")
        result = function(*args, **kwargs)
        string_split = result.split()
        return string_split
    return wrapper

@splitter_decorator	# this is executed next
@lowercase_decorator	# this is executed first
def hello(string):
    print("hello function")
    return string

print(hello("Hello World"))	 # output => [ 'hello' , 'world' ]


# # func = lambda a, b : (a ** b) #what is the output of 
# # print(func(float(10),20))



# def decorator_age(func):
    
#     def wrapper(*args, **kwargs):
#         print("sam", func.__name__)
#         args = list(args)
#         args[0] += 1
#         return func(*args, **kwargs)
#     return wrapper

# @decorator_age
# def normal(age, weight):
#     print("Anki", age, weight)
#     return
# normal(21, 4)
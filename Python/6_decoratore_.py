# decorator function to convert to lowercase
def lowercase_decorator(function):
    def wrapper():
        func = function()
        string_lowercase = func.lower()
        return string_lowercase
    return wrapper

# decorator function to split words
def splitter_decorator(function):
    def wrapper():
        func = function()
        string_split = func.split()
        return string_split
    return wrapper

@splitter_decorator	# this is executed next
@lowercase_decorator	# this is executed first
def hello():
    return 'Hello World'

hello() 	 # output => [ 'hello' , 'world' ]

string = "This is  a string."
string_list = string.split(' ') #delimiter is ‘space’ character or ‘ ‘
print(string_list) #output: ['This', 'is', 'a', 'string.']
print(' '.join(string_list)) #output: This is a string.


func = lambda a, b : (a ** b) #what is the output of 
print(func(float(10),20))



x=1e+5
print(x)


import time

print ("time.time(): %f " %  time.time())
print (time.localtime( time.time() ))
print (time.asctime( time.localtime(time.time()) ))
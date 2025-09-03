#Declare a variable
x=("hello kevin")
print(x)
#global variable
x="awesome"
def my_func():
    print("python is",x)
my_func()
# Create a variable inside a function, with the same name as the global variable
x="kevin"
def my_func():
    x="raj"
    print("hello",x)
my_func()
print("hello",x)    




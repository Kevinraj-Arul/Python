#Simple function
def my_func():
    print("I am Kevin")
my_func()
#using argument and parameter
def my_func(name):
    print("My Name is " +name)
my_func("kevin")
#using aribitary argument
def my_fun(*kid):
    print("The young child is "+kid[2])
my_fun("ramu","raj","Ramesh")
#using keyword argument
def my_fun(**name):
    print("second child " + name["s"])
my_fun(name="raju", s="ramu", t="raghul")
#using return 
def my_func(num):
    return num * num
result =my_func(5) +10
print(result)
def logging(num):
    def wrapper(*args):
        print("start logging")
        num(*args)
        print("ending logging")
    return wrapper
@logging
def add(num1,num2):
    print(num1 +num2)
@logging
def sub(num1,num2):
    print(num1-num2)
add(10,2)
sub(10,2)
#simple class and oject
class name:
    def student(self):
        print("hi I am kevin")
s1=name()
s1.student()
#constructor
class student:
    def __init__(self,name,age):
        self.x=name
        self.y=age
    def __str__(self):
        print(f"My name is :{self.x},My age is :{self.y}")
s1=student("kevin","23")
s1.__str__()
#without constructor
class mathtool:
    def square(self,n):
        return n*n
    def cube(self,n):
        return n*n*n
math=mathtool()
print(math.square(5))
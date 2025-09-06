from abc import ABC, abstractmethod
class owner(ABC):
    @abstractmethod
    def work(self):
        print("go to field for labour1 and go to internal work for labour2")
class labour1(owner):
    def work(self):
        print("I am going to field work")
class labour2(owner):
    def work(self):
        print("I am going to internal work")
l1=labour1()
l2=labour2()

l1.work()
l2.work()
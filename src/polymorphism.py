#Different class with same method
class car:
    def __init__(self,model,year):
        self.model=model
        self.year=year
    def spec(self):
        print("good")
class bus:
    def __init__(self,model,year):
        self.model=model
        self.year=year
    def spec(self):
        print("speed")
class lorry:
    def __init__(self,model,year):
        self.model=year
        self.year=2020
    def spec(self):
        print("load")
v1=car("BmW",2010)
v2=bus("tata",2020)
v3=lorry("asok leyland",2017)

for i in v1,v2,v3:
    i.spec()

#Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:
class vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def spec(self):
        print("brand")
class car(vehicle):
    def spec(self):
        print("speed")
class boat(vehicle):
    def spec(self):
        print("luxzury")

v1=car("BMW",2020)
v2=boat("shipyard",2024)

for i in (v1,v2):
    print(i.brand)
    print(i.year)
    i.spec()




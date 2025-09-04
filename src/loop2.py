#While
i = 1
while i < 6:
    print(i)
    i += 1
#while important 
Correct_pin="123"
enter_pin=" "
while enter_pin!=Correct_pin:
    enter_pin =input("enter your pin:")
print("Granted access")
#while important
iteams=[]

while True:
    iteam =input("add iteam:")
    if iteam.lower() == "done":
        break
    iteams.append(iteam)
print ("iteams in cart",iteams)


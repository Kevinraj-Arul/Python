#simple set
s=["apple","orange","Banana"]
print(set(s))
#iterating set
s=["apple","orange","Banana"]
for i in s:
    print(i)
#sets
cites={"chennai","banglore","delhi","chennai"}
newcites=set(cites)
print(newcites)
#union
cites={"chennai","banglore","delhi","chennai"}
newcites={"pune","gujarat","rajasthan"}
print(newcites.union(cites))
#intersection
cites={"chennai","banglore","delhi","chennai"}
newcites={"pune","gujarat","rajasthan"}
print(newcites.intersection(cites))
#difference
cites={"chennai","banglore","delhi","chennai"}
newcites={"pune","gujarat","rajasthan"}
print(newcites.difference(cites))
cites={"chennai","banglore","delhi","chennai"}
cites.add("hyderabad")
print(cites)

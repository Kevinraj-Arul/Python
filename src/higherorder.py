#map function
fru=["apple","orange","pinaple"]
r=list(map(lambda fru:fru.upper(),fru))
print(r)
#filter
num=[2,14,15,20,25]
n=list(filter(lambda x:x %2==0,num))
print(n)
#reduce
from functools import reduce
num=[1,2,3,4,5]
s=reduce(lambda a,b:a+b,num)
print(s)
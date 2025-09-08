#generator
def number(n):
    for i in range(n):
        yield i
for num in number(6):
    print(num)
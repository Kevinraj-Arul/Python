#Exception with except try name
try:
    number_items=int(input("How many items:"))
    total_price=200 * number_items
    average_price= total_price / number_items
    print("average price :",average_price)
except ZeroDivisionError:
    print("zero cannot divide")
#Exception with except 
try:
    number_items=int(input("How many items:"))
    total_price=200 * number_items
    average_price= total_price / number_items
    print("average price :",average_price)
except Exception:
    print("zero cannot divide")

print("next block of code")

#using finally
try:
    number_items=int(input("How many items:"))
    total_price=200 * number_items
    average_price= total_price / number_items
    print("average price :",average_price)
except FileNotFoundError:
    print("zero cannot divide")
finally:
    print("Logout")

print("next block of code")

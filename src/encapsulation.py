#Abstration 
class order:
    def __init__(self,customer_name,items,total_amount,discount):
        self.customer_name=customer_name
        self.items=items
        self.__total_amount=total_amount
        self.__discount=discount
    def __calculate_final(self):
        return self.__total_amount - self.__discount
    def _admin_view(self):
        return{
            "Customer":self.customer_name,
            "Items":self.items,
            "total_amount":self.__total_amount,
            "discount":self.__discount,
            "final Bill":self.__calculate_final()
        }
    def customer_view(self):
        return{
            "Customer":self.customer_name,
            "Items":self.items,
            "final Bill":self.__calculate_final()
        }
class adminportal:
        def order_view(self ,order):
            return order._admin_view()
class app:
        def customerorder_view(self ,order):
            return order.customer_view()
ORDER=order("kevin",["Juice", "puffs"],100,20)

admin= adminportal()
customer= app()

print("Admin View:")

print(admin.order_view(ORDER))

print("customer view:")

print(customer.customerorder_view(ORDER))
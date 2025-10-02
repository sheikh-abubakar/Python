
class items:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_price(self):
        return self.price*self.quantity
    
class recipt:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def show_recipt(self):
        total = 0
        for item in self.items:
            item_total = item.total_price()
            total += item_total
            print(f"{item.name}(x{item.quantity}) - each: {item.price} =  {item_total}")

        print(f"total amount without discount: {total} ")
        discount = total * 0.2
        final_amount = total - discount
        
        print(f"Discount (20%): {discount}")
        print(f"Final Amount: {final_amount}")



product1 = input("enter product1 you want tot buy: ")
quantity1 = int(input("enter no. of products you want to buy: "))

product2 = input("enter product2 you want tot buy: ")
quantity2 = int(input("enter no. of products you want to buy: "))

product3 = input("enter product3 you want tot buy: ")
quantity3 = int(input("enter no. of products you want to buy: "))

item1 = items(product1, 120, quantity1)
item2 = items(product2, 120, quantity2)
item3 = items(product3, 120, quantity3)


my_recipt = recipt()
my_recipt.add_item(item1) 
my_recipt.add_item(item2) 
my_recipt.add_item(item3)

print("-------RECIPT-------")

my_recipt.show_recipt()

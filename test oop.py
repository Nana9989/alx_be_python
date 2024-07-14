#class definition
class item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
#value
    def value(self):
        return addition

#object
item1 = item("milk", "5.5", "17")
item2 = item("bread", "20", "8")
item3 = item("sugar", "3", "12")
item4 = item("rice", "57", "9")
item5 = item("salt", "2", "300")


#accesing object properties and functions
print(f" {item1.name} costs ghc{item1.price}, we have {item1.quantity} on hand.")
print(f" {item2.name} costs ghc{item2.price}, we have {item2.quantity} on hand.")
print(f" {item3.name} costs ghc{item3.price}, we have {item3.quantity} on hand.")
print(f" {item4.name} costs ghc{item4.price}, we have {item4.quantity} on hand.")
print(f" {item5.name} costs ghc{item5.price}, we have {item5.quantity} on hand.")


addition =float(item1.price) *float(item1.quantity) +float(item2.price) *float(item2.quantity) +float(item3.price) *float(item3.quantity) +float(item4.price) *float(item4.quantity) +float(item5.price) *float(item5.quantity)

print(f"The total value of the stock we have on hand is {addition}")
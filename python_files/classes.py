class item:
    def total_price(self,x,y):
        return x*y
    
item1 = item() # intance of an item
item1.name = "Redmi"
item1.price = 12000
item1.quantity = 2
#print(item1.total_price(item1.price,item1.quantity))

item2 = item()
item2.name = "samsung"
item2.price = 14000
item2.quantity = 4
#print(item2.total_price(item2.price,item2.quantity))
print()
#using constuctor __Init__
# it reduces coding of attributes of an object as in
#  the above senario where every object and its attributed are provided
class item:
        
        def __init__(self,name,price,quantity): # it is called as many times as the number of insance in a class eg when we ha ve 2 insance it will be called 2 times and so on
            #Run validation to the received argument

            assert price >= 0
            assert quantity > 0
        
            #assign to self
            self.name = name
            self.price = price #attributes
            self.quantity = quantity
        def total_price(self):
            return self.price * self.quantity


item1 = item("Redmi",12000,2) # intance of an item
item2 = item("samsung",14000,4)
print(item1.total_price())
print(item2.total_price())
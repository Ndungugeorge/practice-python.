"""class MyList(list):
    def print_sorted(self):
        #print(sorted(self))

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
#print(my_list)
my_list.print_sorted()
#print(my_list)
"""
def is_same_class(obj, a_class):
    return isinstance(obj, a_class)# and type(obj) is a_class

# Example usage:
class ExampleClass:
    pass

obj1 = ExampleClass()
obj2 = "Hello"

print(is_same_class(obj1, ExampleClass))  # True
print(is_same_class(obj2, ExampleClass))  # False
print(type(obj1))
print(type(ExampleClass))
"""
def element_at(my_list, idx):
    if idx <0 :
        return None
    elif idx > len(my_list):
        return None
    return my_list[idx]

my_list = [1, 2, 3, 4, 5]
idx = 5
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

#Write a function that replaces an element of a list at a specific position (like in C).
def replace_in_list(my_list, idx, element):
    if idx <0 :
        return my_list
    elif idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list

my_list = [1, 2, 3, 4, 5]
idx = 5
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)
print(my_list)
print(new_list)

#Write a function that prints all integers of a list, in reverse order.
def print_reversed_list_integer(my_list=[]):
    for i in my_list[::-1]:
        print("{}".format(i))

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
"""
#Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
def new_in_list(my_list, idx, element):
    if idx <0 :
        return my_list
    elif idx >= len(my_list):
        return my_list
    new = [i for i in my_list]
    new[idx]=element
    return new

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
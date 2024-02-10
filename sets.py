"""names = {"George","Mwaura",23,10}

print(type(names))

import string
_ = (lambda x: print(''.join(chr(ord(c) & ~32) for c in x)))(string.ascii_uppercase)
print(dir(string))"""
set1 = {10,20,34,"python","alx"}
set2 = set() #for empty set we use set function
set1.add(12)#add new value in a set we use method
print(set1) #output is unordered
print(len(set1)) # find length of a set
set1.remove(12) #function to remove an element in a set
print(set1)
set1.discard(10)#remove item if element not present it will not bring error message
print(set1)
print(set1.pop()) #this function remove items randomly returning the removed item
print(set1)

#operation on sets
print("Operations on set")
set3 = {"joj","ALX","python","software"}
set4 = {"ALX","mwao","programing","isfun"}

print(set3.union(set4)) # or set3 | set4 union operation combines 2 sets removing the duplicate
set3.update(set4) #updates set without duplicate
print(set3)
set3.update(["mwao","joj"]) #updates the tuple
print(set3)

print(set3.intersection(set4)) #prints duplicate item

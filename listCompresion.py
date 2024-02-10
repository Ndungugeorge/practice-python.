myList = ["apple","banana","orange"]
new = []
for fruit in myList:
    new.append(fruit.upper())
fruit = new
print(fruit)
#using list comprehension
myList=[fruit.upper()for fruit in myList]
print(myList)

#sring manupulation
myStr = "HelloMyNameIsGeorge"
myStr = "".join(i if i.islower() else " " + i for i in myStr)[1:]
print(myStr)
num = [23,21,34,34] #creating a list of int
letter = ["a","b","c","d"]
strg = ["george", "mwaura","pyhon"]
all = ["joji","mwau",23, 'c']
print(all)
print (strg)
print(letter)
print(num)
#list in matrices
mat =[ [1,2],["a","b"]]
print(mat)
#Accessing the list
print(all[0]) #accessing the list
print(all[-4]) #accessing lst from the end of the list
print(all[:3]) #accessing element from 0 upto 3
print(all[3:])#from 3 upto end of list
print(all[::2])#access every 2nd element of list
print(all[::-1]) #access element in reverse order
#writting element in a given number of element
y = [2]*100
print(y)

#concatination of list
cat = all + strg
print(cat)
var = list("Mwaura hi") #unpacking string
print(var)

#operation
num.append(6)
print(num)

num.extend(strg) 
print(num)

num.insert(5,"python")  #insert ata given position
print(num)

num.remove("pyhon")
print(num)

var1 = ["z","y","r","a","m","x"]
var1.sort()
print(var1)


#Exercise
list1 = list(range(1,11)) #or [1,2,3,4,5,6,7,8,9,10] 
#split the list1 into 2 lists odd and even
odd = list1[::2]
even = list1[1::2]
print(list1)
print(odd)
print(even)


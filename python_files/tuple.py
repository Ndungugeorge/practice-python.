"""tp = (12,13,"joji","mwao")
print(tp)
print(tp[1]) #indexing
print(type(tp)) 
#tuples are immutable/unchangeable
print(tp[1:4])  #slicing in tuple
print(len(tp))  #finding length of tuple
print("We are in for loop")
for tuple in tp:
 print(tuple)"""

tuple1 = (0,1,2,3,4,5,6,7,8,9)
tuple2 =  tuple1 + (10,)  #adding an element 10 to tuple1
tuple3 = tuple2 + tuple1[::-1] #concatinating tuple2 with the reverse of tuple1 in i.e slicing

print("tuple1",tuple1)
print("tuple2",tuple2)
print("tuple3",tuple3)
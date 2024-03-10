"""f1 = open("myFile","r")
data = f1.read()
print(data)


# write mode- it override the file if the file alredy exist
# creates a new file if the file does not exist
fl = open("myFile","w")
ptr = fl.write("programming is fun")
print(ptr)


# r+ mode - open the file in both read an write mode
# if file does not exist it does not create any file
# return error FileNotFound if file does not exist
fl = open("myFile","r+")
# tell() shows th position of a pointer
ptr = fl.read()
print(fl.tell())
ptr = fl.write("HI")
print(fl.tell())
print(ptr)

# w+ mode open file in both read and write mode
# override a file if it exists
# create a new file if it does not exist
# seek() moves cursor at a given position
 
# a open file i append mode cant read
# if the file exist add at the end of the file
# if doesnt exist create new file
f1 = open("myFile","a")
data = f1.write(" You are the best")
print(data)
"""
# a+ open file in both append and read
# file handler exists at the end of the file
# creates a new file if the file does not exist
f1 = open("myFile","a+")

f1.seek(0)# moving the cursor from the end
print(f1.read())
data = f1.write(" You are a programmer")
print(data)

# reading binary file we use rb
# writting binary file we use wb
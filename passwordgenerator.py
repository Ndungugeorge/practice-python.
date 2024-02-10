import random
"""
a = (input("Enter the numbers:"))
b = input("Enter the letters:")
c = input("Enter special characters:")

chars = a+b+c
length = len(chars)
z = ''.join(random.choice(chars)for i in range(length))
print("Strong password:",z)
"""

print("Welcome to the Password Generator ")
password= ""

a = int(input("How many letters would you like in your password? :"))

ls1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
for i in range(1,a+1):
  choice = random.choice(ls1)
  password+=choice

b = int(input("How many numbers would you like in your password? :"))

for i in range(1,b+1):
   choice = str(random.randint(1,b))
   password+=choice

c = int(input("How many special char would you like in your password? :"))
ls3 = [',','/','#','@','.','!','}','*']

for i in range(1,c+1):
    choice = random.choice(ls3)
    password+=choice
print(password)





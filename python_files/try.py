"""
a = chr(((ord("f")-ord('a')-1)) + ord('a'))
print(a)
print(chr(101))
print(ord('f'))
number = 98
print(f"{number:d} street batteries")

#!/usr/bin/python3
number = 3.14159
print(f"{number:.3f}")

#!/usr/bin/python3
str = "Holberton School"
print(3*str)
print(str[:9])

#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str1 += " " + str1
print(f"Welcome to {str1}!")

#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[0:3]
word_last_2 = word[7:]
middle_word = word[1:7]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")

#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
#object-oriented programming with Python
str = str[39:66] + str[106:112] + str[:6]
print(str)

import this

import sys

message = "and that piece of art is useful - Dora Korpar, 2015-10-19\n"
sys.stderr.write(message)
sys.exit(1)
"""
"""
#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
    
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_digit= number%10
else:
    last_digit= (-number %10) * -1
if last_digit > 5:
    print(f"last digit of {number} is {last_digit} and is greater than 5")
if last_digit ==0:
    print(f"last digit of {number} is {last_digit} and is 0")
if last_digit <6 and last_digit!=0:
    print(f"last digit of {number} is {last_digit} and is less than 6 and not 0")

def add(a,b):
    return a+b

import dis # bytecodes 
dis.dis(add)
"""
k = [2,1,0,3,0,2,1]
print(k.count(k.index(0)))
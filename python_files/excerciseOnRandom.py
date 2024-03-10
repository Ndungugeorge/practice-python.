import random
# Receive user input as a string
friends = input("Enter a list of names separated by space: ")

# Split the input string into individual names
name_list = friends.split()

# Create a list containing the names
names = name_list

print("list of friends",names)

a = random.choice(names)
#print(f"{a} will pay the bill")
print("{} will pay the bill".format(a))

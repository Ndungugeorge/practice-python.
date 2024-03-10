"""
try:
    value = int(input("Enter the value:"))
    print("value is:{}".format(value))
except ValueError:
    print("Enter valid value")
    

my_list_1 = [1,2,3,34]
my_list_2 = [2,3,2,45]
j = max(len(my_list_1), len(my_list_2))

for i in range(0,j):
    div = my_list_1[i] / my_list_2[i]
    print("{} / {} is: {}".format(my_list_1[i],my_list_2[i],div))
"""
import sys


value = 'gt'
try:
    print("{:d}".format(value))
except (TypeError, ValueError):
    print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)

help(int)




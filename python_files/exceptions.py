try:

    num1, num2 = input("Enter 2 numbers:").split()
    quotent = int (num1) / int (num2)
    print("{}/{}={}".format(num1,num2,quotent))

except ZeroDivisionError as ex:
    print (ex.args)
    print("Can't be divided by zero")
except ValueError:
    print("No enough value to unpack")
else:
    print("No exception")
finally:
    print("Am a programmer")
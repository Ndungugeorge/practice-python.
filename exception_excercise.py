#create a file named mydata.txt
#catch FileNotFoundError
#in else print the content of file
"""try:
    myfile = open("mydata.txt",encoding="utf-8")
except FileNotFoundError:
    print("No such file")
else:
    print("file:",myfile.read())
    myfile.close()
finally:
    print("Done")
"""

try:
    n = 10   
    n1 = 0
    z = n/n1
    print("{}/ {} = {}".format(n,n1,z))
except ZeroDivisionError:
    print("number cant be divided by zero")
else:
    print("{}/ {} = {}".format(n,n1,z))
finally:
    print("well done")
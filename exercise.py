str1 = "it's sunday"
str2 = "have a great day"
str3 = str1[:5]+ str2[5:13]+ str1[5:]
print(len(str1))
print(str3)

#Exercise 2
a =100
b =200
c=a
d=b
a=d
b=c
print(a,b)
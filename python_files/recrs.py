def factorial(n):
    if n ==1:
        return n
    else:
       return (n * factorial(n-1))  
num = 6
print("fact of ",num, "is:",factorial(num))
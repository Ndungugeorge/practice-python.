"""
ls1 = ['we','are','the','dreamers']
ls2 = ['we','make','it','happen']

ls3 = [ls1,ls2]
print(ls3)
ls4 = [[1,2,3],
       [4,5,6],
       [7,8,9]]
print(ls4)

lis = [[8,7],[6,5]]
for p,q in lis:
    print(p+q,end='&')


def no_c(my_string):
    c = 'cC'
    result = " "
    for i in my_string:
        if i != 'c'and i !='C':
            result += i
    return result

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
"""

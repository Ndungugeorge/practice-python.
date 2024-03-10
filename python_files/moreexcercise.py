order = input("What size of pizza do you want?")
cost = 0
if order ==  'small':
    cost = 100
    #print(f"small pizza is {cost} shillins")
elif order =='medium':
    cost=200
    print(f"Medium pizza is {cost}shillings")
else:
    cost=300
    print(f"large pizza is {cost}shillings")

pepperoni = input("do you want pepperoni(y/n)?")
if pepperoni=='y' or pepperoni == 'Y':
    if order == 'small':
        cost = cost + 30
    elif order == 'medium' or order == 'large':
        cost = cost + 50
cheese = input("do you want extra cheese(y/n)?")
if cheese=='y' or cheese == 'Y':
    if order == 'small' or order == 'medium' or order == 'large':
        cost = cost + 20
        print(f"The bill is {cost}")
elif cheese == 'n':
    print(f"bill is {cost}")
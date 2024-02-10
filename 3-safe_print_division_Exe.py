def safe_print_division(a, b):
    try:
        rsult = a / b
    except (ZeroDivisionError,TypeError):
        rsult = None
    finally:
            print("Inside result: {}".format(rsult))
    return rsult
        
a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
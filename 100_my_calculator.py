import sys
import calculator_1 as i

if len(sys.argv) !=4:
    sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

a = int(sys.argv[1])
operator = (sys.argv[2])
b = int(sys.argv[3])

if operator == '+':
   result = i.add(a,b)
elif operator == '-':
    result = i.sub(a,b)
elif operator == '*':
    result = i.mul(a,b)
elif operator == '/':
    result = i.div(a,b)
else:
    sys.stderr.write("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
print("{} {} {} = {}".format(a,operator,b,result))

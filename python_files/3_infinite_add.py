
import sys
result = 0
n = 0
for i in sys.argv:
    if n != 0:
        result += int(i)
    n+=1

print(result)

"""
import sys
result = 0
for i in sys.argv[1:]:
    result += int(i)
print("{}"format(result))
"""
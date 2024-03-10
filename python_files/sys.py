import sys

print(f"my name is {sys.argv[0]}")

print(f"number of argv: {len(sys.argv) -1}")

nOfArg = len(sys.argv[1:])

i = 1
while nOfArg>=i:
    print(f"argv[i]  is {sys.argv[i]}")
    i+=1


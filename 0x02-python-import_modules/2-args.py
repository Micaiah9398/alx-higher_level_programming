#!/usr/bin/python3
def print_arg(argv):
args = sys.argv[1:]
num_args = len(args)
print("Number of argument", end="")
if num_args == 1:
print(": argument", end="")
elif num_args > 1:
print("s: arguments", end="") else:
print("s.", end="")
print()
for i, arg in enumerate(args)
if __name__ == "__main__":
    import sys
print(i+1, ":", arg)

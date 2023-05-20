#!/usr/bin/python3
if __name__ == "__main__":
    import sys
arg = len(sys.argv) - 1
result = 0
for i in range(1, arg + 1):
    result += int(sys.argv[i])
print("{}".format(result))

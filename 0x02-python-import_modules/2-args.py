#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if count == 1:
	    print("1 argument:")
    else:
	    print("{} arguments.".format(args))
    for i in range(1, args + 1):
	    print("{}: {}".format(i, sys.argv[i]))

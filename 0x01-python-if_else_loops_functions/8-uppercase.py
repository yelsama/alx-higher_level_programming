#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 197:
            print("{}".format(i.upper()), end="")
        else:
            print("{}".format(i), end="")

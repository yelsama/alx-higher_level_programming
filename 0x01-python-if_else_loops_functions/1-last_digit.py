#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last = - last
print(f"Last digit of {number:d} is {last:d} and is ", end="")
if last == 0:
    print(f"0")
elif last > 5:
    print(f"greater than 5")
else:
    print(f"less than 6 and not 0")

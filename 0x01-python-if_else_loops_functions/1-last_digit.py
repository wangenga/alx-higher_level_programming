#!/usr/bin/python3
import random
number = random. randint(-10000, 10000)
if number < 0:
    lastd = - 1 * (-number % 10)
else:
    lastd = number % 10
    print("Last digit of {} is {} and is ".format(number, lastd), end="")
        if lastd > 5:
            print("greater than 5")
        elif lastd == 0:
            print("0")
        else:
            print("less than 6 and not 0")

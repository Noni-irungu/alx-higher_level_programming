#!/usr/bin/python3
'''A function that prints numbers 0 -99'''
for y in range(0, 100):
    if y == 99:
        print("{}".format(y))
    else:
        print("{:02}".format(y), end=", ")

#!/usr/bin/python3
'''A function that prints lowercase alphabets except letter 'q' and 'e'''
for x in range(97, 123):
    if chr(x) != 'q' and chr(x) != 'e':
        print("{}".format(chr(x)), end="")

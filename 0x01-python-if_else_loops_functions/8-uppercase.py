#!/usr/bin/python3

def uppercase(str):
    '''prints string in uppercase'''
    for ch in str:
        if 97 <= ch <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")

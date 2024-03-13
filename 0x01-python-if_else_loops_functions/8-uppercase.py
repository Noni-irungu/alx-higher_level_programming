#!/usr/bin/python3

def uppercase(str):
    '''prints string in uppercase'''
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            ch = chr(ord(ch) - 32)
        print("{}".format(ch), end="")
    print("")

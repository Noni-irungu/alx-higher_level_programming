#!/usr/bin/python3

def uppercase(str):
    '''prints string in uppercase'''
    for chrt in str:
        if ord(chrt) >= 97 and ord(chrt) <= 122:
            chrt = chr(ord(chrt) - ord('a') + ord('A'))
        print("{}".format(chrt), end="")
    print("")

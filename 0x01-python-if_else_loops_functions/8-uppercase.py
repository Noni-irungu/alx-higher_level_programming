#!/usr/bin/python3

def uppercase(str):
    '''prints string in uppercase'''
    for chrt in str:
        if ord("a") <= ord(chrt) <= ord("z"):
            chrt = chr(ord(chrt) - 32)
        print("{:s}".format(chrt), end=", ")

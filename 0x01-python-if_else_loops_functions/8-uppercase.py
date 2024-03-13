#!/usr/bin/python3

def uppercase(str):
    '''prints string in uppercase'''
    for ch in str:
        if 'a' <= ch <= 'z':
            char = chr(ord(char) - ord('a') + ord('A'))
        print(char, end="")
    print()

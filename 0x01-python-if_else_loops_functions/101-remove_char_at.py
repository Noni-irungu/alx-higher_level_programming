#!/usr/bin/python3
'''a program that creates a cpy of a string
remving the character at the 'n' position'''
def remove_char_at(str, n):
    if n < 0:
        return str
    else:
        str = str[:n] + str[n+1:]
    return str

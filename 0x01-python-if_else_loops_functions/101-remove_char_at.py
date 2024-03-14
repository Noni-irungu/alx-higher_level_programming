#!/usr/bin/python3

def remove_char_at(str, n):

    '''a program that creates a copy of a string
    removing the character at the 'n' position'''
    if n < 0:
        return str
    else:
        str = str[:n] + str[n+1:]
    return str

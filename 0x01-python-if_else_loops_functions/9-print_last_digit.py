#!/usr/bin/python3

def print_last_digit(number):
    '''prints last digit of number'''
    print(abs(number) % 10, end="")
    return (abs(number) % 10)

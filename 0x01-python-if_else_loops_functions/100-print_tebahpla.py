#!/usr/bin/python3
'''A program that prints the ASCII alphabet in
reverse order, changing lowercase and uppercase'''
for num in range(122, 96, -1):
    if num % 2:
        num = num - 32
    print("{:c}".format(num), end="")

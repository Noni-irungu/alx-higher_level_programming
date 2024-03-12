#!/usr/bin/python3
'''printing different combinations of two digits'''
for v in range(0, 8):
    for h in range(v + 1, 10):
        print("{:d}{:d}".format(v, h), end=', ')
print("{:d}{:d}".format(v + 1, h))

#!/usr/bin/python3

'''Prints the sum of arguments'''

if __name__ == "__main__":

    import sys

    sum_mation = 0
    for i in sys.argv[1:]:
        sum_mation = sum_mation + int(i)
    print("{}".format(sum_mation))

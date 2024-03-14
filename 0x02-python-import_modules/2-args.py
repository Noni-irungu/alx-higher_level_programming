#!/usr/bin/python3

'''Prints the number of arguments
and it's list'''

if __name__ == "__main__":

    import sys

    total = len(sys.argv) - 1
    if total == 0:
        print("0 arguments.")
    elif total == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(total))
    for i in range(total):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

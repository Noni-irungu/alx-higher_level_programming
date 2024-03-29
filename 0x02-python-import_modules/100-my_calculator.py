#!/usr/bin/python3

'''Imports functions from file calculator_1.py
file and handles basic arithmetic operations'''

if __name__ == "__main__":

    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv[1:]
    argv_total = len(argv)
    oprt = {"+": add, "-": sub, "*": mul, "/": div}

    if argv_total != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in oprt:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif sys.argv[2] == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif sys.argv[2] == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif sys.argv[2] == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

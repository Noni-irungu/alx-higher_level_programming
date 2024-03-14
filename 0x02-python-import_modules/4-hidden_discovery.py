#!/usr/bin/python3

'''Prints names defined in the given module'''

import hidden_4

na_mes = dir(hidden_4)
for na_me in na_mes:
    if na_me[:2] != "__":
        print(na_me)

#!/usr/bin/python3

'''Prints names defined in the given module'''

if __name__ == "__main__":

    import hidden_4

    na_mes = dir(hidden_4)

    for nam_e in na_mes:
        if nam_e[:2] != "__":
            print(nam_e)

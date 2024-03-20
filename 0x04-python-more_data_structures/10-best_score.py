#!/usr/bin/python3

'''A function that returns a key with the
biggest integer value'''


def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    rtn_ky = list(a_dictionary.keys())[0]
    big_gest = a_dictionary[rtn_ky]
    for m, n in a_dictionary.items():
        if n > big_gest:
            big_gest = n
            rtn_ky = m
        return (rtn_ky)

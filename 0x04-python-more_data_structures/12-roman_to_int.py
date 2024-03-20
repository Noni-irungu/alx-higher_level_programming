#!/usr/bin/python3

'''A function that converts a Roman numeral
to an integer'''


def roman_to_int(roman_string: str):
    if roman_string is not None or not isinstance(roman_string, str:
            return 0
    rmn_d= {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nums= [rmn_d[x] for x in roman_string] + [0]
    rmn_num= 0

    for j in range(len(roman_string) - 1):
        if nums[j] >= nums[j+1]:
            rmn_num += nums[j]
        else:
            rmn_num -= nums[j]
    return rmn_num

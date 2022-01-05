#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        uni = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        comb = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        convert = 0
        roman_comb = ""
        i = 0
        while i < len(roman_string):
            if i + 1 < len(roman_string):
                roman_comb = roman_string[i] + roman_string[i+1]
            if roman_comb in comb:
                convert += comb[roman_comb]
                i += 1
            elif roman_string[i] in uni:
                convert += uni[roman_string[i]]
            i += 1
        return convert
    else:
        return 0

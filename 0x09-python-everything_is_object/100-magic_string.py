#!/usr/bin/python3
def magic_string(it=[0]):
    it[0] += 1
    return "BestSchool" + ", BestSchool" * (it[0] - 1)

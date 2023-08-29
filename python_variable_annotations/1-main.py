#!/usr/bin/env python3
"""Testing for type-annotaded function - concat"""
concat= __import__('1-concat').concat

str1 = "Hello"
str2 = "World"

print(concat(str1, str2)) == "{}{}".format(str1, str2)  # True
print(concat.__annotations__) == {'str1': str, 'str2': str, 'return': str}  # True
print("concat(str1, str2) returns", concat(str1, str2))  # True
print(concat(str1, 2))  # False
print(concat(2, str2))  # False

"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

chris alan
Sample Output

Chris Alan
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    result = []
    capitalize_next = True  # Flag to indicate if the next letter should be capitalized

    for i, char in enumerate(s):
        if capitalize_next and char.isalpha():  # Capitalize if it's the start of a word
            # Check if the previous character is a number
            if i > 0 and s[i - 1].isdigit():
                result.append(char.lower())  # Keep the letter lowercase if the previous character is a number
            else:
                result.append(char.upper())  # Capitalize the letter
            capitalize_next = False
        elif char == ' ':  # After a space, the next letter should be capitalized
            result.append(char)
            capitalize_next = True
        else:
            result.append(char)  # Keep digits and other non-alphabet characters as is

    return ''.join(result)

if __name__ == '__main__':

    s = str(input())

    result = solve(s)
    print(result)
  

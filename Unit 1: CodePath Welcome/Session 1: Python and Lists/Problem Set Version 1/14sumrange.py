'''
Problem 14: Total Sum in Range
Write a function sum_range() that returns the sum of numbers from a given start value to a given stop value 
(inclusive).

def sum_range(start, stop):
    pass
Example Usage: sum = sum_range(3, 9)
Example Result: sum = 42

Command to run this file:
python3 14sumrange.py
''' 

def sum_range(start, stop):
    sum = 0
    for i in range (start, stop + 1):
        sum = sum + i
    return sum

result = sum_range(3, 9)
print (result)
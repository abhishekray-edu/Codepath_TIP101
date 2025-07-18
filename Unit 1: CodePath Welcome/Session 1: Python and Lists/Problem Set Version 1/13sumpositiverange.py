'''
Problem 13: Total Sum
Write a function sum_positive_range() that returns the sum of numbers from 1 to a given stop value (inclusive).

def sum_positive_range(stop):
    pass
Example Usage: sum = sum_positive_range(6)
Example Result: sum = 21

Command to run this file:
python3 13sumpositiverange.py
''' 

def sum_positive_range(stop):
    sum = 0
    for i in range(1, stop +1):
        sum = sum + i
    return sum

result = sum_positive_range(6)
print(result)


'''
def sum_positive_range_optimal(stop):
    n = stop
    return n*(n + 1)//2

result = sum_positive_range_optimal(6)
print(result)
'''
'''
Problem 12: Sum of 1 to 10
Write a function sum_ten() that returns the sum of numbers from 1 to 10.

def sum_ten():
    pass
Example Usage: output = sum_ten()
Example Result: output = 55

Command to run this file:
python3 12sumten.py
''' 

def sum_ten():
    sum = 0
    for i in range (1,11):
        sum = sum + i
    return sum

result = sum_ten()
print(result)

'''
def sum_ten_optimal():
    n = 10 
    return n*(n+1)//2

result = sum_ten_optimal()
print(result)
'''
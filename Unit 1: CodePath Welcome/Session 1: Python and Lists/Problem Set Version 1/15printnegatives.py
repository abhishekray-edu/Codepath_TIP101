'''
Problem 15: Negative Numbers
Write a function print_negatives() that takes a list of integers lst and prints all negative numbers in the list.

def print_negatives(lst):
Example Usage: print_negatives([3,-2,2,1,-5])
Example Output:

-2
-5
Example Usage: print_negatives([1,2,3,4,5])
Example Output:

None

Command to run this file:
python3 15printnegatives.py
''' 

def print_negatives(lst):
    flag = False
    for num in lst:
        if num < 0:
            print (num)
            flag = True
    if not flag:
        print (None)

print_negatives([1,2,-3,4,-5])
print_negatives([1,2,3,4,5])
'''
Problem 10: Last Item
Write a function get_last() that takes in a list as a parameter and returns the last item in the list. 
Return None if the list is empty.

def get_last(lst):
    pass
Example Input: [3,1,6,7,5]
Example Output: 5

Command to run this file:
python3 10lastitem.py
''' 

def get_last(lst):
    return lst[-1] if lst else None

result = get_last([3,1,6,7,5])
print (result)
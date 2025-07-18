'''
Problem 9: First Item
Write a function get_first() that takes in a list as a parameter and returns the first item in the list. 
Return None if the list is empty.

def get_first(lst):
    pass
Example Input: [3,1,6,7,5]
Example Output: 3

Note: pass is a keyword that is used as a placeholder for future code

Command to run this file:
python3 9firstitem.py
''' 

def get_first(lst):
    return lst[0] if lst else None

result = get_first([12, 77, 99])
print (result)
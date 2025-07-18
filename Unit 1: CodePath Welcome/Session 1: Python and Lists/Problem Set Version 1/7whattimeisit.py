'''
Problem 7: What time is it?
Let's put what we learned in Problems 1-4 all together! Write a function named what_time_is_it() 
that takes an integer hour as a parameter.
If hour is 2, the function should return "taco time 🌮".
If hour is 12, the function should return "peanut butter jelly time 🥪”.
Otherwise, the function should return "nap time 😴".

Example Usage:

time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time)
Output:

taco time 🌮
nap time 😴
peanut butter jelly time 🥪

Command to run this file:
python3 7whattimeisit.py
''' 
def what_time_is_it(hour):
    if hour == 2:
        return "taco time 🌮"
    elif hour == 12:
        return "peanut butter jelly time 🥪 "
    else:
        return "nap time 😴"


time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time)
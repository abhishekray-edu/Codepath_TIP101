'''
Problem 8: Blackjack
In the game Blackjack, players try to draw a hand of cards that totals as close to 21 as possible. 
Players "bust" if their cards total more than 21. Players say "Hit me!" if they want the dealer to give them another card.

Write a function called blackjack() that takes an integer score as a parameter.
If score equals 21, print "Blackjack!".
If score is greater than 21, print "Bust!".
If score is greater than or equal to 17 and less than 21, print "Nice hand!".
If score is less than 17, print "Hit me!".

Example Usage:

blackjack(24)
blackjack(19)
blackjack(21)
blackjack(10)
Output:

Bust!
Nice Hand!
Blackjack!
Hit me!

Command to run this file:
python3 8blackjack.py
''' 
# 0   17  21 
def blackjack(score):
    if score == 21:
        print ("Blackjack!")
    elif score > 21:
        print ("Bust!")
    elif (score >= 17):
        print("Nice hand!")
    else:
        print ("Hit me!")


blackjack(24)
blackjack(19)
blackjack(21)
blackjack(10)
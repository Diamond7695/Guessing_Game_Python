"""A number-guessing game."""
from random import randint
# Put your code here

name = input("Howdy, What's your name?\n")
user_name = name
print("my name is " + " " + user_name)
print(user_name + ", I'm thinking of a number between 1 and 100.\n")

game = int(input("Try to guess my number\n"))

attempts = 0




guessing_number = randint(1, 100)

while True:
    guessing_the_number = input("your guess?\n")
    
    guessing_the_number = int(guessing_the_number)
        
    if guessing_the_number < guessing_number:
            print("Your guess is too low, try again.")
            attempts += 1
    else: 
        if guessing_number > guessing_number:
         print("Your guess is too high, try again")
        else:
                 print("Well Done, " + user_name + " You found my number!")
                 print(f'You found my number in {attempts} tries!')
                 break
            
           
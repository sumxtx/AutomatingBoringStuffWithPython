#Guess the number:

import random


machine_guess = random.randint(1,20)
print('I\'m thinking of a number between 1 and 20.')
guesses = 0

while True:
    #print(machine_guess)
    print('Take a guess: ')
    guess = int(input())
    guesses += 1
    
    if guess == machine_guess:
        print('Good Job! You guessed my number in ' + str(guesses) + ' guesses!')
        break




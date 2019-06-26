# This is a guess the number game.

import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number from 1 through 20.')

#Ask the player to guess 5 times.
for guessesTaken in range(1, 6):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low dude.')
    elif guess > secretNumber:
        print('That guess is a bit too high.')
    else:
        break     #This is the correct guess
    
if guess == secretNumber:
    print('Nice! You gussed the number in ' + str(secretNumber))
else:
    print('Nope, you failed, again. The number was ' + str(secretNumber))
        

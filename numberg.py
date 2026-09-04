#Creating a Number guessing game

import random

n=random.randint(1,100)

for i in range(5):
    g=int(input("Guess the number (1 to 100):"))

    if g<n:
        print("Too Low!")

    elif g>n:
        print('Too High!')

    else:
        print('Correct Guess')
        break
    
else:
    print("You ran out of attempts!!!")
    print("The number was:",n)
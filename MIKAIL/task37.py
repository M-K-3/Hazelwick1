import random

num = random.randint(1, 100)

guess = -2
while guess != num:
    guess = int(input("Guess a number: "))
    if guess == num:
        print("Correct")
    elif guess < num:
        print("Too low.")
    else:
        print("Too high.")
import random

num = random.randint(1, 100)

guess = int(input("Guess a number: "))
while guess != num:
    if guess == num:
        print("Correct")
    elif guess < num:
        print("Too low.")
    else:
        print("Too high.")
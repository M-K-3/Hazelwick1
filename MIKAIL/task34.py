import random
score = 0

num1 = random.randint(1, 100)
guess1 = int(input("Enter your first guess: "))
if guess1 == num1: 
    print("Bang-on!")
    score = score + 10
elif num1 - 5 <= guess1 <= num1 + 5:
    print("Close.")
    score = score + 5
elif num1 - 10 <= guess1 <= num1 + 10:
    print("Okay.")
    score = score + 2
elif num1 - 10 > guess1 or guess1 > num1 + 10:  
    print("Way off.")
    score = score + 0


num2 = random.randint(1, 100)
guess2 = int(input("Enter your second guess: "))
if guess2 == num2:
    print("Bang-on!")
    score = score + 10
elif num2 - 5 <= guess2 <= num2 + 5:
    print("Close.")
    score = score + 5
elif num2 - 10 <= guess2 <= num2 + 10:
    print("Okay.")
    score = score + 2
elif num2 - 10 > guess2 or guess2 > num2 + 10:
    print("Way off.")
    score = score + 0

num3 = random.randint(1, 100)
guess3 = int(input("Enter your third guess: "))
if guess3 == num3:
    print("Bang-on!")
    score = score + 10
elif num3 - 5 <= guess3 <= num3 + 5:
    print("Close.")
    score = score + 5
elif num3 - 10 <= guess3 <= num3 + 10:
    print("Okay.")
    score = score + 2
elif num3 - 10 > guess3 or guess3 > num3 + 10:
    print("Way off.")
    score = score + 0

num4 = random.randint(1, 100)
guess4 = int(input("Enter your fourth guess: "))
if guess4 == num4:
    print("Bang-on!")
    score = score + 10
elif num4 - 5 <= guess4 <= num4 + 5:
    print("Close.")
    score = score + 5
elif num4 - 10 <= guess4 <= num4 + 10:
    print("Okay.")
    score = score + 2
elif num4 - 10 > guess4 or guess4 > num4 + 10:
    print("Way off.")
    score = score + 0


num5 = random.randint(1, 100)
guess5 = int(input("Enter your fifth guess: "))
if guess5 == num5:
    print("Bang-on!")
    score = score + 10
elif num5 - 5 <= guess5 <= num5 + 5:
    print("Close.")
    score = score + 5
elif num5 - 10 <= guess5 <= num5 + 10:
    print("Okay.")
    score = score + 2
elif num5 - 10 > guess5 or guess5 > num5 + 10:
    print("Way off.")
    score = score + 0

print("Your score is", score)

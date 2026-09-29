score = 0
A1 = int(input("What is 8+10?"))

if A1 == 18:
    print("Correct!")
    score = score + 1
else:
    print("Incorrect. The answer is 18.")

A2 = int(input("What is 5-6?"))
if A2 == -1:
    print("Correct!")
    score = score + 1
else:
    print("Incorrect. The answer is -1.")

A3 = int(input("What is 7*9?"))
if A3 == 63:
    print("Correct!")
    score = score + 1
else:
    print("Incorrect. The answer is 63.")

A4 = int(input("What is 12/3?"))
if A4 == 4:
    print("Correct!")
    score = score + 1
else:
    print("Incorrect. The answer is 4.")
print("Your score is:", score, "out of 4.")
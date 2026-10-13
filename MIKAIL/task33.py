number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
    print("Divisible by 3, 5 and 7.")
elif number % 3 == 0 and number % 5 == 0 and number % 7 != 0:
    print("Divisible by 3 and 5.")
elif number % 3 == 0 and number % 7 == 0 and number % 5 != 0:
    print("Divisible by 3 and 7.")
elif number % 5 == 0 and number % 7 == 0 and number % 3 != 0:
    print("Divisible by 5 and 7.")
elif number % 3 == 0 and number % 5 != 0 and number % 7 != 0:
    print("Divisible by 3.")
elif number % 5 == 0 and number % 3 != 0 and number % 7 != 0:
    print("Divisible by 5.")
elif number % 7 == 0 and number % 3 != 0 and number % 5 != 0:
    print("Divisible by 7.")
elif number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
    print("Not divisible by 3, 5 or 7.")
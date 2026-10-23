while True:
    guess = 0
    while guess < 100:
        num = int(input("Enter a number: "))
        guess += num

    print(f"Final total: {guess}")
    break
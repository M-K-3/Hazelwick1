hours = 1

while hours != 0:
    hours = int(input("How many hours have you been parked? "))
    electric = input("Is your car electric? ")

    if electric == "yes":
        charge = hours * 2
        print(f"Your charge is £{charge}.")
riders = 0

while riders <= 8:
    height = int(input("Enter the rider's height in centimetres:"))
    if height < 120:
        print("They cannot ride.")
    elif height >= 120 and height < 140:
        adult = input("Are they riding with an adult? ")
        if adult == "yes":
            print("They can ride.")
            riders = riders + 1
        elif adult != "yes":
            print("They cannot ride.")
    elif height >= 140:
        print("They can ride.")
        riders = riders + 1
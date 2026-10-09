temp = int(input("Enter the temperature in Celsius: "))
if temp < 0:
    print("Freezing")
elif temp >= 0 and temp < 21:
    print("Cold")
elif temp >= 21 and temp < 31:
    print("Warm")
else:
    print("Hot")
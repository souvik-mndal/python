temp = float(input("Enter temperature in Celsius: "))

if temp < 0:
    print("Freezing Cold")
elif temp <= 10:
    print("Very Cold")
elif temp <= 20:
    print("Cold")
elif temp <= 30:
    print("Pleasant")
elif temp <= 40:
    print("Hot")
else:
    print("Very Hot")
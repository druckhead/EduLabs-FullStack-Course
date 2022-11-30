age = int(input("Enter your age: "))
height = int(input("Enter your height in cm: "))

if (age >= 8 and age <= 18 and height >= 115) or (age > 18 and height > 100):
    print("You can ride this rollercoaster")
else:
    print("You cant ride this rollercoaster")
import math

decimal1 = math.fabs(float(input("enter a number: ")))
decimal2 = math.fabs(float(input("enter another number: ")))

wholeNumber = int(decimal1) - int(decimal2)
decimalTotal = decimal1 + decimal2

print(decimalTotal - wholeNumber)
feet1 = int(input("enter the feet: "))
inches1 = int(input("enter the inches: "))
feet2 = int(input("enter the feet: "))
inches2 = int(input("enter the inches: "))
feetTotal = feet1 + feet2
inchesTotal = inches1 + inches2

if inchesTotal >= 12:
  print("feet: " + str(feetTotal + 1) + "inches: " + str(inchesTotal - 12))

else: print("feet: " + str(feetTotal) + " inches: " + str(inchesTotal))
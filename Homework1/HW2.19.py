#Alvin Nguyen 2055636
#input
lemon = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
anectar = float(input("Enter amount of agave nectar (in cups):\n"))
servs = float(input("How many servings does this make?\n"))
#output
print("\nLemonade ingredients - yields {:.2f} servings".format(servs))
print("{:.2f} cup(s) lemon juice".format(lemon))
print("{:.2f} cup(s) water".format(water))
print("{:.2f} cup(s) agave nectar".format(anectar))
#input desired servings
deserv=float(input("\nHow many servings would you like to make?\n"))
#Lemonade ingredients
print("\nLemonade ingredients - yields {:.2f} servings".format(deserv))
print("{:.2f} cup(s) lemon juice".format(lemon*deserv/servs))
print("{:.2f} cup(s) water".format(water*deserv/servs))
print("{:.2f} cup(s) agave nectar".format(anectar*deserv/servs))
#convert to gallons
print("\nLemonade ingredients - yields {:.2f} servings".format(deserv))
print("{:.2f} gallon(s) lemon juice".format(lemon*deserv/servs/16))
print("{:.2f} gallon(s) water".format(water*deserv/servs/16))
print("{:.2f} gallon(s) agave nectar".format(anectar*deserv/servs/16))



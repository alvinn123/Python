#Alvin Nguyen 2055636
#(1)
import math
hwall = int(input("Enter wall height (feet):\n"))
wwall = int(input("Enter wall width (feet):\n"))
area = hwall * wwall
print("Wall area:", area, "square feet")
#(2)
paintneed = area/350
print("Paint needed:", '{:.2f}'.format(paintneed), "gallons")
#3
print("Cans needed:", math.ceil(paintneed),"can(s)")
#4
pColor = {"red": 35,"blue": 25,"green": 23}
color = input("\nChoose a color to paint the wall:\n")
print("Cost of purchasing",color, "paint:", "$"+'{}'.format(pColor[color]*math.ceil(paintneed)))

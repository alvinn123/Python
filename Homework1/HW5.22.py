#Alvin Nguyen 2055636
#(1) Starting menu
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")
#2 User input 2 services
service1 = input("Select first service:\n")
service2 = input("Select second service:\n")
print("")
#3 and 4 Output service and cost

print("Davy's auto shop invoice\n")
cost = 0
#Service 1
if service1 == "Oil change":
    print("Service 1: Oil change, $35")
    cost = cost + 35
elif service1 == "Tire rotation":
    print("Service 1: Tire rotation, $19")
    cost = cost + 19
elif service1 == "Car wash":
    print("Service 1: Car wash, $7")
    cost = cost + 7
elif service1 == "Car wax":
    print("Service 1: Oil change, $12")
    cost = cost + 12
elif service1 == "-":
    print("Service 1: No service")
    cost = cost + 0
else:
    print("Please re-enter your service")
#Service 2
if service2 == "Oil change":
    print("Service 2: Oil change, $35\n")
    cost = cost + 35
elif service2 == "Tire rotation":
    print("Service 2: Tire rotation, $19\n")
    cost = cost + 19
elif service2 == "Car wash":
    print("Service 2: Car wash, $7\n")
    cost = cost + 7
elif service2 == "Car wax":
    print("Service 2: Car wax, $12\n")
    cost = cost + 12
elif service2 == "-":
    print("Service 2: No service\n")
    cost = cost + 0
else:
    print("Please re-enter your service")
#Total Cost
print('Total: ${}'.format(cost))
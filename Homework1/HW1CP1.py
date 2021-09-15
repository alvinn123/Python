#Alvin Nguyen 2055636
#input date
month = int(input("What is the current month?"))
day = int(input("What is the current day?"))
year = int(input("What is the current year?"))
#input birthday date
bmonth = int(input("What is the month of your birthday?"))
bday = int(input("What is the day of your birthday?"))
byear = int(input("What is the year of your birthday?"))
#Calculate Age
age = year - byear
#Check birthday
if month == bmonth and day == bday:
    print("Happy Birthday!")
#output
print("Birthday Calculator")
print("Current day")
print("Month:", month)
print("Day:", day)
print("Year:", year)
print("Birthday")
print("Month:", bmonth)
print("Day:", bday)
print("Year:", byear)
print("You are", age, "years old.")

# Alvin Nguyen 2055636

# dictionary for players

p_dict = {}

# Ask for player and jersey number 5 times in loop

for i in range(5):
    number = int(input("Enter player " + str(i + 1) + "'s jersey number:\n"))
    rating = int(input("Enter player " + str(i + 1) + "'s rating:\n"))
    print("")
    p_dict[number] = rating

print("ROSTER")
# Output player roster
for i in sorted(p_dict.keys()):
    print("Jersey number: " + str(i) + ", Rating: " + str(p_dict[i]))
print("")

while True:
    # Output menu
    print(
        "MENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit")
    print("")
    print("Choose an option:")
    # Ask for user input

    option = input()

    # To add the new player in the dictionary

    if option == 'a':
        number = int(input("Enter a new player's jersey number:\n"))
        rating = int(input("Enter the player's rating:\n"))
        p_dict[number] = rating

    # delete player

    elif option == 'd':
        number = int(input("Enter a jersey number:\n"))
        del p_dict[number]

    # To update the players rating in the dictionary

    elif option == 'u':
        number = int(input("Enter a jersey number:\n"))
        rating = int(input("Enter a new rating for player:\n"))
        p_dict[number] = rating

    # output roster

    elif option == 'o':
        print("ROSTER")
        for i in sorted(p_dict.keys()):
            print("Jersey number: " + str(i) + ", Rating: " + str(p_dict[i]))

    # output players above a rating

    elif option == 'r':
        rating = int(input("Enter a rating: \n"))
        print("ABOVE " + str(rating))
        for i in p_dict.keys():
            if p_dict[i] > rating:
                print("Jersey number : " + str(i) + ", Rating: " + str(p_dict[i]))

    # Stops the code
    elif option == 'q':
        break

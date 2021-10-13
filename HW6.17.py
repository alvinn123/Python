# Alvin Nguyen 2055636
# user input
word = input()
password = ''
# replace characters using if statements
for i in range(len(word)):
    if 'i' in word[i]:
        password += '!'
    elif 'a' in word[i]:
        password += '@'
    elif 'm' in word[i]:
        password += 'M'
    elif 'B' in word[i]:
        password += '8'
    elif 'o' in word[i]:
        password += '.'
    else:
        password += word[i]
# append/adding q*s to end of the password
password += 'q*s'
# output
print(password)

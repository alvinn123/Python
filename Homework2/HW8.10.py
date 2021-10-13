# Alvin Nguyen 2055636
# user input
phrase = input("")
forward = ""
backward = ""
# start loop
for i in phrase.lower():
    if i != ' ':  # check for spaces
        forward += i
        backward = i + backward
# If input is the same as forward and backward output that it is a palindrome
if forward == backward:
    print(phrase + " is a palindrome")
# otherwise confirm it is not a palindrome
else:
    print(phrase + " is not a palindrome")

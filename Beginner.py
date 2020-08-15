isPalindrome = False
while not isPalindrome:
    name = input("Enter a word and see if it's a Palindrome\n\n")
    nameReversed = name[name.__sizeof__()::-1]
    if name != "" and name == nameReversed:
        isPalindrome = True
        print("Palindrome!!!!!!!!!!!!!!!!!!")
    else:
        print("Not Palindrome!!!!!!!!!!!!!!")
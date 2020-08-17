def palindrom():
    isPalindrome = False
    while not isPalindrome:
        name = input("Enter a word and see if it's a Palindrome\n\n")
        nameReversed = name[name.__sizeof__()::-1]
        if name != "" and name == nameReversed:
            isPalindrome = True
            print("Palindrome!!!!!!!!!!!!!!!!!!")
        else:
            print("Not Palindrome!!!!!!!")


def isPerfectNumber():
    perfectNumber = input("Please enter a perfect number\n\n")
    lengthOfPerfectNumber = perfectNumber.__len__()
    additionOfPerfectNumber = 0
    for x in perfectNumber:
        additionOfPerfectNumber += int(x)
    result = additionOfPerfectNumber ** lengthOfPerfectNumber

    if (result == int(perfectNumber)):
        print ("This number is perfect")


def isNombreParfait():
    nombreParfait = int(input ("Enter a perfect number\n"))
    somme = 0
    for x in range(1, nombreParfait):
        if (nombreParfait % x == 0):
            somme += x
    if (somme == nombreParfait):
        print ("Le nombre est parfait!!!!")
    else:
        print("Le nombre saisi n'est pas parfait!!!!")


def isPerfectNum(num):
    pow, num_temp, sum = len(str(num)), num, 0

    while num_temp != 0:
        sum = sum + (num_temp % 10) ** pow
        num_temp = num_temp / 10

        print("Perfect num") if sum == num else False


isPerfectNum(2)
##isNombreParfait()
##isPerfectNumber()
##palindrom()
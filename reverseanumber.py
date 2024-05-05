# python algorithm

# reverse a number digits position


# String version reverse number
def reverseANumberString(userNum):
    print("Reverse a number using a string.")
    userNumArray = list(str(userNum))
    output = "".join(userNumArray[::-1])
    return output
# print(reverseANumberString(4567))
# reverseANumberString()


# math base 10 reverse a number
# https://www.geeksforgeeks.org/write-a-program-to-reverse-digits-of-a-number/#
def reverseANumberMath(userNum):
    print("Reverse a number using modulus.")
    revNum = 0
    while userNum > 0:
        revNum = (revNum * 10) + (userNum % 10)
        userNum = userNum // 10
    return revNum
# print(reverseANumberMath(4567))
# reverseANumberMath()


def repeat():
    print("Please input an integer")
    userNumber = int(input())
    print("")
    print("This algorithm uses the string method to reverse an integer:")
    print(reverseANumberString(userNumber))
    print("")
    print("This algorithm uses the math base 10 method to reverse an integer:")
    print(reverseANumberMath(userNumber))
    print("")
    
    print("Would you like to test another number? (Y/N)")
    yesNo = input().upper()
    if(yesNo == "Y"):
        print("")
        repeat()
    else:
        print("")
        print("Goodbye")

repeat()

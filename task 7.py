

#task A

def wordsread():

    file = open("SDD - Task 7 - Text Files/hello.txt", "r")
    words = file.read()
    file.close()

    return words

word = wordsread()
print(word)


def readpassword():

    file = open("SDD - Task 7 - Text Files/password.txt", "r")
    password = file.read()
    file.close()

    return password


def checkpassword(wordpass):

    print("what is your password")
    userpassword = input()

    for counter in range(0,3):
        if userpassword == wordpass:
            print("access granted")
            break

        else:
            print("access denied")
            print("what is your password")
            userpassword = input()

    return userpassword



wordpass = readpassword()
passworduser = checkpassword(wordpass)



def readnum():

    file = open("SDD - Task 7 - Text Files/lottery.txt", "r")
    lotnum = file.read()
    array = lotnum.split(" ")
    file.close()

    return array

def checknum(lotterynum):

    usernums = [""]
    total = 0

    print("what are your lottery numbers")
    usernums = input()
    splitUnums = usernums.split(" ")


    for i in splitUnums:

        if splitUnums[i] in lotterynum:
            total +=1

    if total == 0:
        print("None of your numbers match, you won nothing")

    elif total == 1:
        print("2 of your numbers match, you won £10")

    elif total == 2:
        print("3 of your numbers match, you won £25")

    elif total == 3:
        print("4 of your numbers match, you won £50")

    elif total == 4:
        print("5 of your numbers match, you won £100")

    elif total == 5:
        print("All of your numbers match, you won £500")



    return usernums

lotterynum = readnum()
unums = checknum(lotterynum)

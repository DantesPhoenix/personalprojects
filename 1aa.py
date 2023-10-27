import re

def readata():

    file = open("test.txt", "r")
    fileData = file.read()
    splitData = fileData.split()

    return splitData


def translate(splitData):

    vowls = ["A","a","E","e","I","i","O","o","U","u"]

    for counter in range(len(splitData)):
        if splitData[counter][0] in vowls:
            splitData[counter] = splitData[counter] + "-yay"

        else:
            fLetter = splitData[counter][0]
            pigWord = splitData[counter][1:]

            splitData[counter] = pigWord + "-" + fLetter + "ay"


    print(splitData)


dataReturn = readata()
translate(dataReturn)

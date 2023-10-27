
#defining function
def getname():

    #getting users intended name
    targetname = input("enter target name: ")

    return targetname

#defining function
def countocc(tname, array):

    #defining variables to store occurrences of each name
    occurence = 0

    #looping for length of array
    for i in range(len(array)):

        #adding 1 to each counter when name is in the array
        if array[i] == tname:
            occurence = occurence + 1

    return occurence

#defining procedure
def printoccur(toccurred):

    #printing no of times name occurs in array
    print("The name you entered is in the array ", toccurred, " times")

    #printing confirmation that name does not exist in array
    if toccurred == 0:
        print("the name you entered does not exist in the array")


#defining array with names inputed
array = ["jon", "doe", "bob", "doe", "mamma", "mamma", "yo", "mamma", "deez", "jack"]

#main program
tname = getname()
toccurred = countocc(tname, array)
printoccur(toccurred)


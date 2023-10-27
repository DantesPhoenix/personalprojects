#task A

#importing libraries
from random import randint



#defining function to get random numbers and store them in an array
def getranum():

    #defining array
    array = [0]*25

    #25 random integers from -250 to 250
    for i in range(25):
        array[i] = randint(-250, 250)

    return array

#defining function to find max number in array
def findmax(randarray):

    maxarray = max(randarray)

    return maxarray


#main programm
randarray = getranum()
maximarray = findmax(randarray)
print(maximarray)

#task B






#Correction for Python Level 1 Assignment 

#check the firstletter if vowel or consonant 


# -----------------------------------------------------------------------------------

# Input the name 

myName = input("Please type your official first name: \n")

# -----------------------------------------------------------------------------------

newFirst = myName.lower()


if newFirst == myName.lower():
    firstLetter = newFirst[0]
    print("This is your name scrambled \n")
    newName = newFirst + firstLetter 
    print(newName[1:])


else:
    print = (myName)


# -----------------------------------------------------------------------------------

if firstLetter in 'aeiou':

    #add ean to the name

    newName = newFirst + 'ean' # angela + ean = angelaean

    print("This is your name scrambled \n")
    
    print(newName)


else:

    newName = newFirst + 'ay'

    print("This is your name scrambled \n")

    print(newName[1:])


# -----------------------------------------------------------------------------------

#Create new file
#Save as Functions.py
#Save in Python-Level-2 folder ---- repo(repository)

#Add two numbers

def AddNumbers(x,y):       #Definition of the function

    return x + y


#Call our Function

Total = AddNumbers(4,9)

#Output the results

print(f"The sum total is = {Total}")

#Ask the user for inputs from the keyboard

num1 = int(input("Enter any number \n"))

num2 = int(input("Enter another number \n"))

#Call the function once again

sum = AddNumbers(num1,num2)

#Print the sum 

print("The sum now of {0} plus {1} is equal to {2}".format(num1, num2, sum))
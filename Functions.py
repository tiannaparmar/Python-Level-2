#Create new file
#Save as Functions.py
#Save in Python-Level-2 folder ---- repo(repository)

#Add two numbers

def AddNumbers(x,y,z):       #Definition of the function

    return x + y + z

def GetSquares(x):
    
    return x * x


#Call our Function

Total = AddNumbers(4,9,100)

#Output the results

print(f"The sum total is = {Total}")

#Ask the user for inputs from the keyboard

num1 = int(input("Enter any number \n"))

num2 = int(input("Enter another number \n"))

num3 = int(input("Enter another number again \n"))

#Call the function once again

sum = AddNumbers(num1,num2,num3)

#Print the sum 

print("The sum now of {0} plus {1} plus {2} is equal to {3}".format(num1, num2, num3, sum))

#Call the squares function

print(GetSquares(4))

square = GetSquares(16)


print("The square is", square)  

#A function that calculates the area of a Circle

def AreaofCircle(r):
    PI = 3.142      #declared a constant --- whose values don't change --- static -- uppercase

    return (PI * r * r)



#function call

area = AreaofCircle(14)

#display the results

print("The area is =",area)


#function definition

def AreaOfRectangle(): #No parameters

 l = eval(input("Enter the value for the length of your rectangle \n")) #prompt user inputs for the length  
 w = eval(input("Enter the value for the width of your rectangle \n")) #prompt user for width

 Area = l * w 

 print("Area of rectangle is", Area)

#function call

AreaOfRectangle()

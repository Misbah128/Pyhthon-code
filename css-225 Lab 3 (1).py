#Syed Hussain
#07/22/2022

print("Hello World") #This program prints Hello World to the screen

name = input("What is your name: ")
print("Hello,", name)
#This program that asks the user for their name and greets them with their name.

name = input("What is your name: ")
if name == "Farhan Sofi" or name == "Syed Hussain":
 print('Hello,' + name);
 #only the users Syed Hussain and Farhan sofi are greeted with their names.

pi = 3.14
r = int(input("Please enter radius of the circle: "))
r = float(r)
Area = pi * r ** 2
print("Area of the circle is: ", Area)
 #This program that will compute the area of a circle. Prompt the user to enter the radius
#and print a nice message back to the user with the answer.

miles = int(input("How many miles driven on thw car: "))
gallon = int(input("How many gallon of gas did you use: "))
mpg = (miles/gallon)
print("Your car delivers", mpg, "miles per gallon of fuel.")
#This program will compute MPG for a car.
# Prompt the user to enter the number of miles driven and the number of gallons used.
# Print a nice message with the answer

fahrenheit = float(input("Please enter temperature in fahrenheit: "))
Celsius = (fahrenheit * 9/5) + 32
print("The tempertaure in Celsius is: ", Celsius)
#This program will convert degrees Fahrenheit to degrees Celsius.

start_day = int(input("From 0-6, what day is it?"))
days_to_wait = int(input("How many days are you gone?"))
end_day = (start_day + days_to_wait) % 7
print(end_day)
#this program which asks for the starting day number, and the length of your stay,
# and it will tell you the number of day of the week you will return on.

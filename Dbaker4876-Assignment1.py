#Name:                  Dbaker4876-Assignment1.py
#Author:                Derek Baker
#Date Created:          06-02-2023
#Date Last Modified:    06-02-2023
#
#Purpose:
#This program will help Arnold take orders from customers and calculate the cost of the order
#The program will ask for what they want to order, ask them to confirm their order, and then print them a reciept 

answer = input("WELCOME TO ARNOLD'S AMAZING EATS!! ARE YOU HERE TO ORDER FOOD OR WHAT? [Y/N]: ").lower()

if answer == "n":
    exit() 

firstName = input("Please enter your first name: ")

lastName = input("Please enter your last name: ")

streetNumber = input("Please enter your street number: ")

streetName = input("Please enter your street name: ")

apartmentNum = input("Please enter your unit # if applicable: ")

city = input("Please enter your city: ")

province = input("Please enter your province: ")

postalCode = input("Please enter your postal code: ")

specInstructions = input("Please enter any special instructions: ")

phoneNum = input("Please enter your phone number: ")

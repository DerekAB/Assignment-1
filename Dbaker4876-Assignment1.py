#Name:                  Dbaker4876-Assignment1.py
#Author:                Derek Baker
#Date Created:          06-02-2023
#Date Last Modified:    06-02-2023
#
#Purpose:
#This program will help Arnold take orders from customers and calculate the cost of the order
#The program will ask for what they want to order, ask them to confirm their order, and then print them a reciept 

din1 = "Austin's pemeal bacon"
din2 = "Aaron's poutine"

def getDinnerOrder():
    dinner = float(input("Which dinner would you like? \n[1 - " + din1 + "] \n[2 - " + din2 + "] \n"))
    if dinner == 1:
        dinner = din1
        price = 15
    if dinner == 2:
        dinner = din2
        price = 10
        
    quantity = int(input("How many would you like?: "))  
      
    totalPrice = price * quantity
    
    if totalPrice == range(100 - 500):
        disPrice = totalPrice * 0.1
    if totalPrice > 500:
        disPrice = totalPrice * 0.2
    if totalPrice < 100:
        disPrice = totalPrice * 0.15
    
    savings = totalPrice - (totalPrice + disPrice) 
    grandTotal = totalPrice - disPrice
    print('                           ')
    print(dinner + " * " + str(quantity))
    print('                             ')
    print('----------------------------')
    print('                                  ')
    print("Total " + str(totalPrice))
    print("Discount " + str(savings))
    print("Grand total " + str(grandTotal))
    
    confirm = input("Is this what you want?: ")
    if confirm == "n":
        return True
    if confirm == "y":
        return False
    



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

while getDinnerOrder():
    if True:
        print("Please reenter your order.")
        
student = input("Are you a student? [Y/N]: ")


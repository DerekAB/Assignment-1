#Name:                  Dbaker4876-Assignment1.py
#Author:                Derek Baker
#Date Created:          06-02-2023
#Date Last Modified:    07-02-2023
#
#Purpose:
#This program will help Arnold take orders from customers and calculate the cost of the order
#The program will ask for what they want to order, ask them to confirm their order, and then print them a reciept 


din1 = "Austin's pemeal bacon"                      #defining the variables so they can be called later
din2 = "Aaron's poutine"

def formatBill(data, headers, size) :               #Creating a function that will format the reciept at the end
    lines = ""
    line = ""
    i = 1
    
    for header in headers :                         #Loop creates space between headers
        line += header + "|"
        while len(line) < size * i :
            line += " "
        i += 1
        
    lines = line + "\n"                             
    lineLength = len(line)
    
    for x in range(1, lineLength):                  #Seperates headers from the body of the table
        lines += "_"
    lines += "\n"
    
    for row in data:                                #Loop through the list of lists and formats it into the table
        line = ""
        i = 1
        for element in row:
            line += element
            while len(line) < size * i :
                line += " "
            i += 1
        lines += line + "\n"
        
    return lines

def getDinnerOrder():                                                                                           #Function is for asking the user which dinner they want and then
    global dinner, price, totalPrice, tax, grandTotal, quantity                                                 #calculating how much it will cost. 
    dinner = float(input("Which dinner would you like? \n[1 - " + din1 + "] \n[2 - " + din2 + "] \n"))
    if dinner == 1:
        dinner = din1
        price = 15
    if dinner == 2:
        dinner = din2
        price = 10
    
    quantity = float(input("How many would you like?: "))  
      
    totalPrice = price * quantity
    
    
    if totalPrice == range(100 - 500):                      #Price calculations based on the total amount of the bill and adding the discounts
        disPrice = round(totalPrice * 0.2, 2)
    if totalPrice > 500:
        disPrice = round(totalPrice * 0.25, 2)
    if totalPrice < 100:
        disPrice = round(totalPrice * 0.15, 2)
    
    savings = totalPrice - (totalPrice + disPrice) 
    grandTotal = totalPrice - disPrice
    
    print('                           ')
    print(dinner + " * " + str(quantity))                   #Printing the reciept to the user and asking for confirmation
    print('                             ')
    print('----------------------------')
    print('                                  ')
    print("Total $" + str(totalPrice))
    print("Discount $" + str(savings))
    print("Grand total $" + str(grandTotal))
    
    confirm = input("Is this what you want? [Y/N]: ")
    if confirm == "n":
        return True
    if confirm == "y":
        return False
    
answer = input("WELCOME TO ARNOLD'S AMAZING EATS!! ARE YOU HERE TO ORDER FOOD OR WHAT? [Y/N]: ").strip().lower()  #This is the first thing the user will see, and asks if they want to order some food

if answer == "n":
    exit() 

firstName = input("Please enter your first name: ")

lastName = input("Please enter your last name: ")

streetNumber = input("Please enter your street number: ")                                   #Getting the user's information

streetName = input("Please enter your street name: ")

apartmentNum = input("Please enter your unit # if applicable: ")

city = input("Please enter your city: ")

province = input("Please enter your province: ")

postalCode = input("Please enter your postal code: ")

specInstructions = input("Please enter any special instructions: ")

phoneNum = input("Please enter your phone number: ")

while getDinnerOrder():                                                                 #Calling the function to determine their order
    if True:
        print("Please reenter your order.")
        
studentDiscount = round(grandTotal * 0.1, 2) 
studentDif = round(grandTotal - (grandTotal + studentDiscount), 3)                      #Calculating the discounts if they say 'yes' to be a student
studentDis = round(grandTotal - studentDiscount, 2)
tax = totalPrice * 0.13

headers = ["Order", "Item Amount", "Item Price", "Total"]               #Setting the headers for the formatBill function

student = input("Are you a student? [Y/N]: ").strip().lower()               #Asking if the user is a student or not
if student == "y":
    endPrice = round(tax + studentDis, 3)
    print(firstName + ' ' + lastName)
    print(streetNumber + ' ' + streetName + ' ' + ' ' + apartmentNum)       #If the user says 'yes' to being a student, it will present a reciept adding in the discount
    print(city + ', ' + province + ', ' + postalCode)
    print(specInstructions)
    print("")
    data = [dinner, str(quantity), '$' + str(price), '$' + str(grandTotal)], ['10% Student Savings', '', '', str(studentDif)], ['', '', 'Sub Total', str(studentDis)], ['', '', 'Tax (13%)', str(tax)], ['', '', 'Total', str(endPrice)]
    print(formatBill(data, headers, 30))
    
if student == "n":
    endPrice = round(tax + grandTotal, 3)
    print(firstName + ' ' + lastName)
    print(streetNumber + ' ' + streetName + ' ' + ' ' + apartmentNum)           #If the user says 'no' to being a student, the program will present a reciept without the student discount.
    print(city + ', ' + province + ', ' + postalCode)
    print(specInstructions)
    print("")
    data = [dinner, str(quantity), '$' + str(price), '$' + str(grandTotal)], ['', '', 'Sub Total', str(grandTotal)], ['', '', 'Tax (13%)', str(tax)], ['', '', 'Total', str(endPrice)]
    print(formatBill(data, headers, 25))
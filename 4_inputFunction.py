# input() -> input function that prompts the user to enter data, returns the input data as 'string'

gender = int(input("\n\nAre You a\n1. girl?\n2. Boy\n: "))
if gender == 1:
    bs = "Sis"
else:
    bs = "Bro"

name = input(f"\nWhat is your Name {bs}!\n: ")
# here age is a string, not int so we have to make convert it to be an integer
age = int(input(f"Enter Your age {bs}!\n: "))

print("\nAssalamu Alikum!")
print(f"{bs}, {name},\nThank You for joining us, we learned your age is {age}!\n")


print(f"{bs} do you want to exit or continue?")
exitOrNot = int(input("1.Exit\n2.Continue\n: "))

import sys 
if exitOrNot == 1:
    sys.exit() #everything below it is ignored, and it terminates execution, best for scripts, CLI tools, controlled exits
    #notes:
    '''
    fully stop script -> use sys.exit()
    inside a funciton -> return
    debuggin/force stop -> raise
    example : raise Exception("Stopping execution")
    '''   
else:
    print("Do you want to:")
    print("1--Rectangle Area Calculate!--")
    print("2--Shopping cart program!-----")
    print("3--Sum of 2 number------------")
    whattodo = int(input(": "))
    if whattodo == 1:
            ######################################################################
            # Exercise 1 Rectangle Area Calculate
            # Area = Width X Length 
            # 1---Rectangle Area Calculate---
            unit = input("Unit: ")
            len = float(input("length: "))
            wid = float(input("width: "))
            area = len * wid
            print()
            print(f"Area of the Rectangle: {area} {unit}²\n")
            
            # Windows:
            # Hold Alt and type 0178 → ²
            # Hold Alt and type 0179 → ³              

            # macOS:
            # Press Control + Command + Space → open emoji & symbol viewer
            # Then search "superscript 2" or "superscript 3" → ² ³
        
            # print("\u00B2")  # ²
            # print("\u00B3")  # ³


    elif whattodo == 2:
        #########################################################################
        # Exercise 2 shopping cart program
        print("------Shopping cart program!------")
        curency = input("What is the curency?: ")
        item = input("What item would you like to buy?: ")
        price = float(input("What is the price?: "))
        quantity = int(input("How many you like/want?: "))
        total = price * quantity
        print()
        print(f"You have bought {quantity} x {item}/s")
        print(f"You have to pay: {total} {curency}.")
        
    elif whattodo == 3:
        ##########################################################################
        num1 = int(input("Enter first Number: "))
        num2 = int(input("Enter Second Number: "))
        sum = num1 + num2
        print(f"Sum = {sum}")
    else:
        sys.exit()
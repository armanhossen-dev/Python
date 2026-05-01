#if = do some code only if some condition is True,
#else do something else

print("\nWelcome to the bank Account Page for credit card")
age = int(input("\nEnter your age: "))

if age > 100:
    print("You are too old to sing up")
    
elif  age >= 18: # if age is more or same as 18y then go to the next step;
    #any code underneath the if statement should be indented!
    # print("Your age is ok!")
    print("You are eligible to sign up!")

elif age < 0: #else if
    print("Age cannot be negative!")
    print("You haven't been born yet!")

# elif age > 100:
#   print("You are too old ot sign up")
    # there is a problem with this condition, as the first condition is like 
    # age >= 18: so you will sign up, so after accepting that condition this will not work as wanted so 
    # we should move this conditon that too old person will not sign up to the top or first conditon

else:
    # print("You are too young, call your mom!")
    print("You must be 18+ to sign up")

print()


# ------------------------------------------------------
resp = input("Would you like to have a coffee? (Y/N)\n: ").lower().strip()

#string_variable.lower() = makes that string variable every letter to be lowercase
# og = "ARMAN"
# low = og.lower()
# print(low) #arman
#string_variable.strip()= removes any extra spaces from the very beginnign and very end of that string variable

# if resp.lower() == 'y':
# if resp in ('y', 'Y', 'yes', 'Yes'):
# if resp == 'y' or resp == 'Y':
if resp == 'y':
    print("You will have your coffee in a minute!")

# elif resp == 'n' or resp == 'N':
elif resp == 'n':
    print("Then you can get a glass of water!")

else:
    print("I didn't quite catch that, but let's assume you want water!")    
    
print()


# ------------------------------------------------------    
name = input("Enter Your name: ")
if name == "": #no input just pressed enter
    print("Name cann't be empty!")
    print("You entered nothing!")
    
elif name != "":
    print(f"Hello {name}")
    
else:
    print("Invalid input")

print()


# ------------------------------------------------------    
fr_sale = True
if fr_sale == True:
    print("This BMW is for sale! Want To buy it?")
    yn = input("yes/no: ").lower().strip()
    
    if yn == "yes":
        print("You have to pay 1,20,000$ for this car")
    elif yn == "no": 
        print("You should know the price for now, It's  1,20,000$")
    else:
        print("Invalid input")
else:
    print("Invalid input")

print()
# ------------------------------------------------------   
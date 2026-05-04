# some conditions
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contains digits

print("# 1. username is no more than 12 characters\n# 2. username must not contain spaces\n# 3. username must not contains digits\n")

user = input("Enter your username: ")

length = len(user)
if 0 < length < 13:
    # if " " not in user:    
    if user.find(" ") == -1: #if it doesn't finds ' ' then returns -1
        if user.isalpha() == True: # .isalpha() also checks spaces so we handel it before .isalpha()
        # .isalpha() returns boolean, if a strings only contains alphabest then True
            print(f"Welcome '{user}', [valid username, thanks]")
        else: 
            print("username contains digits, Not valid username!")
    else:
        print("username contains spaces, not valid")
else:
    print("username can not be more than 12 character")
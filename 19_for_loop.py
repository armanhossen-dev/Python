# for loops = execute a block of code a fixed number of times
            # you can iterate over a range, string, sequence, etc
# for counterVariable in range(starting,ending+1):
# inside for loop to go forward or increas we use 'range(start, end+1)' funciton
# inside for loop if we go backward then we use 'reversed(range(s, e+1))'
# if we want to get more like add every time 2 then we use step, range(s, end+1, step)

# #numbers multiple table
n = int(input("\nEnter a number: "))
for i in range(1,11): # this range will set value of i from 1 to 10, when it reach to 11 then it stops
    print(f"{i} X {n} = {i*n}")
    
# Enter a number: 5
# 1 X 5 = 5
# 2 X 5 = 10
# 3 X 5 = 15
# 4 X 5 = 20
# 5 X 5 = 25
# 6 X 5 = 30
# 7 X 5 = 35
# 8 X 5 = 40
# 9 X 5 = 45
# 10 X 5 = 50

# print("Hello") #By default, print() ends with a newline:
# print("Hello", end="\n")

su = 0
ct = int(input(("\nEnter number to count: ")))
for c in range(1, ct+1):
    su += c
    if c == 1:
        print(f"{c} ", end="")
    else:
        print(f"+ {c} ", end="")
print(f" = {su}")
# Enter number to count: 6
# 1 + 2 + 3 + 4 + 5 + 6  = 21

print("\nCount Backwards")
b = int(input("Enter a number: "))
for bb in reversed(range(0, b+1)):
    print(f"{bb} ", end="")
    if bb == 0:
        print()
# Count Backwards
# Enter a number: 9
# 9 8 7 6 5 4 3 2 1 

x = int(input("\nEnter an integer: "))
if x%2 == 0:
    print(f"All even number to from 2 to {x}: ", end="")
    for i2 in range(2, x+1, 2):
        if i2 == 2:
            print(f"{i2}", end="")
        else:
            print(f", {i2}", end="")
    print(".\n")
    # Enter an integer: 8
    # All even number to from 2 to 8: 2, 4, 6, 8.
else:
    print(f"All odd number to from 1 to {x}: ", end="")
    for i3 in range(1, x+1, 2):
        if i3 == 1:
            print(f"{i3}", end="")
        else:
            print(f", {i3}", end="")
    print(".\n")
    # Enter an integer: 5
    # All odd number to from 1 to 5: 1, 3, 5.
     
# we can iterate over a string  
credit_card = "1234-5678-9101-2345"
print(f"Given String: {credit_card}")
for x in credit_card:
    if x!= 0:
        print(f"{x},", end="")
print()

print("\nLets Find Prime Numbers!")
limit = int(input("Enter limit to find: "))
for i in range(1, limit+1):
    x = i
    s = 0
    for a in range(1, i+1):
        if x%a == 0:
            s+=1
    if s <= 2:
        print(f"{x} ", end="")
        # Enter limit to find: 010
        # 1 2 3 5 7 
        # print(f"{x} is a prime number;")        
# Lets Find Prime Numbers!
# Enter limit to find: 10
# 1 is a prime number;
# 2 is a prime number;
# 3 is a prime number;
# 5 is a prime number;
# 7 is a prime number;
print()
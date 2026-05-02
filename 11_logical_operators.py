# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be true
#                     and = both conditions must be true
#                     not = inverts the conditon 
# they are used in (if, elif) conditions
print()
# or between condition, any condition if true then it makes the total condition True
temp = int(input("Enter the temp: "))
isRaining = False
print()
# if temp > 35 or temp < 0 or isRaining == True:
if temp > 35 or temp < 0 or isRaining:
    print("The outdoor event is cancelled!\n")
else:
    print("The outdoor even is still scheduled.\n")


# and , between condition, both side should be True then the total condition is True
# isSunny = True
isSunny = False

if temp >= 28 and isSunny:
    print("It is HOT outside 🥵")
    print("It is SUNNY ☀️")
elif temp <= 0 and isSunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY ☀️")
elif 28 > temp > 0 and isSunny: ##########
    print("It is WARM outside 🙂")
    print("It is SUNNY ☀️")
elif 28 > temp > 0 and not isSunny: 
    #if isSunny is false then = not isSunny -> True
    print("It is WARM outside 🙂")
    print("It is CLOUDY ☁️")
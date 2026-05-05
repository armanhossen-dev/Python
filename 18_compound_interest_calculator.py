# interest is the monetary charge for the privilege of borrowing money.
# interest expense or revenue is often expressed as a dollor amount, whlie the interest rate used to. calculate interest is typically expressed as an annual percentage rate(apr)
# interest is the amount of money a lender or financial institution receives for lending out money
# it can also refer to the amount of ownership a stockholder has in a companyy, usally expressed as a percentage.

# formula: A = P*pow((1 + (r/n)), t)
# A = final amount, P = initial principal balance, r = interest rate, t = number of time periods elapsed

principle = 0
rate = 0
time = 0

# while principle/rate/time cann't be zero, here it works
# but if we use = 0  then there could be problems 

ch = int(input("If calculate interest press 1 or : "))

if ch == 1:
    # while principle <= 0:
    while True:
        principle = float(input("Enter the principle amount: "))
        if principle <= 0:
            print("Principle can't be less than or equal to zero")
        else:
            break
    # print(f"Principle amount = {principle}")

    # while rate <= 0:
    while True:
        rate = float(input("Enter the interest rate: "))
        if rate <= 0:
            print("Interest rate can't be less than or equal to zero")
        else:
            break
    # print(f"Your interest rate is : {rate}")

    # while time <= 0:
    while True:
        time = int(input("Enter time in years: ")) #int years
        if time <= 0:
            print("Time  can't be less than or equal to zero")
        else:
            break
        
    # print(f"Interest time is : {time} years\n")
    n = 100 # as rate is always in 100% so
    total = principle * pow(1 + (rate/n), time)
    print(f"Balance after {time} year/s : ${total:.2f}")
else:
    while True: #it works always, it's a infinte loop until it beaks, every time we use while True, then we have to apply condition and use break to break that loop        
        name = input("Enter a name: ")
        if name == "":
            print("Your name cannot be empty")
        else:
            print(f"Your Name: {name}")
            break
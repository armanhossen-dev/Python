#add temperature converter, add weight converter, add currency converter -- done!
print()
print("What to convert?")
print("1. Temperature:(K, F, C)")
print("2. Weight Conversion (kg ⇄ lb)")
print("3. Currency :BDT(৳), USD($), EUR(€), CNY(¥), GBP(£)")
opt = int(input("Chose what to do(1,2,3): "))
print()

if opt == 1:
    print("Temperature:(K, F, C)")
    print("1. K to F, C")
    print("2. F to C, K")
    print("3. C to F, K")
    ch = int(input("Enter choice (1,2,3): "))
    print()
    
    # windows Alt + 0176 = °
    # macOS   shift + option + 8 = °
    
    if ch == 1:
        k = float(input("K = "))
        c = k - 273.15
        f = (9/5)*c + 32
        # print(f"{f:.2f}") = will give 2 digit after decimal point 
        print(f"F = {f:.2f}°F\nC = {c:.2f}°C")
        
    elif ch == 2:
        f = float (input("F = "))
        c = (5/9)*(f-32)
        k = c + 273.15
        print(f"C = {c:.2f}°C\nK = {k:.2f}")
        
    elif ch == 3:
        c = float(input("C = "))
        f = (9/5)*c + 32
        k = c + 273.15
        print(f"F = {f:.2f}°F\nK = {k:.2f}")
    else:
        print("Invalid choice\n")
        
# print(f"weight = {round(weight,2)} {unit}.\n") this makes error, even if there is unit not valid then it runs so i add this line inside the if statements

elif opt == 2:
    print("Weight Conversion (kg ⇄ lb)\n")
    #kg(kilogram) -> metric system
    #lb(pound) -> imperial system 
    # 1 kg = 2.20462 lb
    
    weight = float(input("\nEnter Your Weight: "))
    unit = input("Choose unit (kg or lb): ").lower().strip()
    print()
    if unit == "kg":    #its kG so converting it into pounds
        weight = weight * 2.20462
        unit = "Lbs"
        print(f"weight = {round(weight,2)} {unit}.\n")

    elif unit == "lb":  #its pounds so converting it into kilograms
        weight = weight / 2.20462
        unit = "Kgs"
        print(f"weight = {round(weight,2)} {unit}.\n")

    else: 
        print(f"{unit} is not valid\n")
        
elif opt == 3:
    print("Chose Currency:")
    print("1.BDT(৳)\n2.USD($)\n3.EUR(€)\n4.CNY(¥)\n5.GBP(£)")
    cur = int(input("Enter choice (1,2,3,4,5): "))
    print()
    
    if cur == 1:
        money = float(input("Enter amount(৳): "))        
        usd = money * 0.009
        euro = money * 0.008
        yuan = money * 0.007
        gbp = money * 0.007
        print(f"USD = {usd:.2f}$")
        print(f"EUR = {euro:.2f}€")
        print(f"Yuan = {yuan:.2f}¥")
        print(f"GBP = {gbp:.2f}£")        
                
    elif cur == 2:
        money = float(input("Enter amount($): "))        
        bdt = money * 125
        euro = money * .95
        yuan = money * 7.3
        gbp = money * 0.80
        print(f"BDT = {bdt:.2f}৳")
        print(f"EUR = {euro:.2f}€")
        print(f"Yuan = {yuan:.2f}¥")
        print(f"GBP = {gbp:.2f}£")
                
    elif cur == 3:
        money = float(input("Enter amount(€): "))        
        bdt = money * 145
        usd = money * 1.1
        yuan = money * 8.0
        gbp = money * 0.87
        print(f"BDT = {bdt:.2f}৳")
        print(f"USD = {usd:.2f}$")
        print(f"Yuan = {yuan:.2f}¥")
        print(f"GBP = {gbp:.2f}")        
        
    elif cur == 4:
        money = float(input("Enter amount(¥): "))        
        bdt = money * 16
        usd = money * 0.14
        euro = money * 0.13
        gbp = money * 0.11
        print(f"BDT = {bdt:.2f}৳")
        print(f"USD = {usd:.2f}$")
        print(f"EUR = {euro:.2f}€")
        print(f"GBP = {gbp:.2f}£")
                
    elif cur == 5:
        money = float(input("Enter amount(£): "))        
        bdt = money * 155
        usd = money * 1.30
        euro = money * 1.18
        yuan = money * 9.0
        print(f"BDT = {bdt:.2f}৳")
        print(f"USD = {usd:.2f}$")
        print(f"EUR = {euro:.2f}€")
        print(f"Yuan = {yuan:.2f}¥")
       
    else:
        print("Invalid choice\n")
    
else:
    print("Invalid choice\n")    
    
#in future improvements use functions
# def temperature_converter():
#     ...
# def weight_converter():
#     ...
# def currency_converter():
#     ...
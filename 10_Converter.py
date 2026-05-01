#add temperature converter, add weight converter, add currency converter

weight = float(input("\nEnter Your Weight: "))
unit = input("Choose unit (kg or lb): ").lower().strip()

#kg(kilogram) -> metric system
#lb(pound) -> imperial system 
#1 kg = 2.2046226lb
if unit == "kg":
    #its kG so converting it into pounds
    weight = weight * 2.205
    unit = "Lbs"
    print(f"weight = {round(weight,2)} {unit}.\n")

elif unit == "lb":
    #its pounds so converting it into kilograms
    weight = weight / 2.205
    unit = "Kgs"
    print(f"weight = {round(weight,2)} {unit}.\n")

else: 
    print(f"{unit} is not valid")

# print(f"weight = {round(weight,2)} {unit}.\n") this makes error, even if there is unit not valid then it runs so i add this line inside the if statements
# https://youtu.be/ix9cRaBkVe0?t=4193
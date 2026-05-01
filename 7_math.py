import math

print(f"pi = math.pi = {math.pi}")
print(f"e = math.e = {math.e}")

#sqrt
print(f"x = 9, √9 = math.sqrt(x) = {math.sqrt(9)}") #3.0

#ceil - it rounds a number up to the nearest int, no matter what the decimal part is
print(f"x = 3.4, math.ceil(x) = {math.ceil(3.4)}") # 4

#floor - it rounds a number down to the nearest int, (toward negative infinity)
a = math.floor(-2.2)
print(f"math.floor(-2.2) = {a}") 
# https://youtu.be/ix9cRaBkVe0?t=2787
print()
print()
print("Lets Calculate Using math module:")
print("1.Calculate Circumference of a circle!")
print("2.Calculate Area of a circle!")
print("3.Calculate Hypotenuse of a right angle triangle!") #pythagorean
choice = int(input("Enter What to do: "))

if choice == 1:
    print("\n----Circumference of a circle-----")
    # c = 2*pi*r
    radius = float(input("Enter radius of circle, r = "))
    c = 2 * math.pi * radius 
    print(f"The circumference or that circle is, c = {round(c,2)}cm")

elif choice == 2:
    print("\n----Area of a circle-----")
    r = float(input("radius of the circle, r = "))
    areaC = math.pi*pow(r,2)
    print(f"Area of the circle is, Area = {round(areaC, 2)}cm²")

elif choice == 3:
    print("\n----Hypotenuse of Right Angle Triangle----") #pythagorean
    a1 = float(input("a = "))
    b1 = float(input("b = "))
    c1 = math.sqrt(pow(a1,2)+pow(b1,2))
    print(f"Hypotenuse of Right Angle Triangle is\nc = √(a²+ b²) = {round(c1, 2)}")
    
else:
    print("Invalid Input!")
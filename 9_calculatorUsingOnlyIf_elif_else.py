#python calculator
#import math 
# +, -, *, /
print()    
operator = input("Enter an Operator (+ - * / ): ")
num1 = float(input("num1 = "))
num2 = float(input("num2 = "))

# print(num1 + operator + num2)  It doesn't happen. also typecasting the int(operator) as operators +, -, *, / are not integer
if operator == '+':
    result = num1 + num2

elif operator == '-':
    result = num1 - num2

elif operator == '*':
    result = num1 * num2

elif operator == '/':
    result = num1 / num2
else:
    print("Invald operator!")
 
print(f"\nnum1 {operator} num2 = {result}\n")
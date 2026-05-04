# format spacifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number)  = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# :  = insert a space before possitive numbers
# :, = comma separator

# examples:
price1 = 168204
price2 = -3030.5
price3 = 43200.45769

print("\n[1] variable:.2f, variable:.20f, variable:.3f")
print(f"Price 1 = ${price1:.2f}") # Price 1 = 168204.00
print(f"Price 2 = ${price2:.20f}") # Price 2 = $-3030.50000000000000000000 -> 20 decimal digit
print(f"Price 3 = ${price3:.3f}") # Price 3 = 43200.468

print("\n[2] variable:20")
# variable:(num) = minimum width (total space) reserved for the number, including its own digits.
print(f"Price 1 = ${price1:20}") # Price 1 = $              168204
print(f"Price 2 = ${price2:20}") # Price 2 = $             -3030.5
print(f"Price 3 = ${price3:20}") # Price 3 = $         43200.45769

print("\n[3] variable:015")
# : → formatting starts
# 5 → total width
# 0 (optional) → fill with zeros instead of spaces
print(f"Price1 = {price1:015}") # Price1 = 000000000168204
print(f"Price2 = {price2:015}") # Price2 = -000000003030.5
print(f"Price3 = {price3:015}") # Price3 = 000043200.45769

print("\n[4] variable:+")
# if i hava any positive value and want to dispay with plus sign then use :+
print(f"Price1 = ${price1:+}") # Price1 = $+168204
print(f"Price2 = ${price2:+}") # Price2 = $-3030.5
print(f"Price3 = ${price3:+}") # Price3 = $+43200.45769

print("\n[5] : ")
# if we want all the positive number to be spaced 1 insted of showing + sign, we use ': '
# by this way the negative remains as it is and the positve values are spaced to allign the negative value
print(f"Price1 = ${price1: }") # Price1 = $ 168204
print(f"Price2 = ${price2: }") # Price2 = $-3030.5
print(f"Price3 = ${price3: }") # Price3 = $ 43200.45769

# 1000 separator, ':,'
print("\n[6] :,")
print(f"Price1 = ${price1:,}") # Price1 = $168,204
print(f"Price2 = ${price2:,}") # Price2 = $-3,030.5
print(f"Price3 = ${price3:,}") # Price3 = $43,200.45769
print(f"Price3 = ${price3:,.2f}") # Price3 = $43,200.46
# print(f"Price3 = ${price3:.2f,}") # X no this will not work

print("\n[7] :+,.2f")
print(f"Price1 = ${price1:+,.2f}")
print(f"Price2 = ${price2:+,.2f}") 
print(f"Price3 = ${price3:+,.2f}") 
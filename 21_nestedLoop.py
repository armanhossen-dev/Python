# nested loop = a loop within another loop (outer, inner)
# outer loop: #(any loop while, for, ..)
#.       inner loop: # (any ...)

#lets display a right angle triangle
rows = int(input("Enter number of rows: "))
column = int(input("Enter number of column: "))
symbol = input("Enter a symbol to use: ")
for a in range(rows): #row
    for b in range(column): #column
        if b <= a:
            print(f"{symbol}", end="")  # print(" * ", end="")
        else:
            break
    print()
# tuple is orderd and unchangeable, tuple is faster than list

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*", 0, "#"))

print("Lets Print it:")
for row in num_pad:
    # print(row)
    # (1, 2, 3)
    # (4, 5, 6)
    # (7, 8, 9)
    # ('*', 0, '#') # but i need to print it without ()
    for num in row:
        print(num, end=" ")
    print()
    # 1 2 3 
    # 4 5 6 
    # 7 8 9 
    # * 0 # 
# 2d collection
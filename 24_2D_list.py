import signal
signal.signal(signal.SIGINT,signal.SIG_IGN)

# 1D list
fruits = ["apple", "orange", "banana", "coconuts"] 
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

# 2D list
groceries = [fruits, vegetables, meats]


# changing a list element, we use index operator[]
fruits[0] = "mango"
#print a list
print(fruits) # ['mango', 'orange', 'banana', 'coconuts']

#printing 2d list
# we will get indivisual list seperate with a comma in a line between []
print(groceries) 
# [['mango', 'orange', 'banana', 'coconuts'], ['celery', 'carrots', 'potatoes'], ['chicken', 'fish', 'turkey']]

# if i use index operator with 2d list
print()
# fruits
print(groceries[0])
['mango', 'orange', 'banana', 'coconuts']

# vegetables
print(groceries[1])
['celery', 'carrots', 'potatoes']

# meats
print(groceries[2])
['chicken', 'fish', 'turkey']

# if i want an element not the lislt then i have to use 2 index operator
print(f'groceries[0][0] = {groceries[0][0]}') # groceries[0][0] = mango
print()

# another way to make 2d list 
groups = [["Arman", "Saief", "Hasib", "Sabbir"],
          ["Rahul", "Bornil", "Sabit", "Riyad"],
          ["Rakib", "Pappu", "Ajmain", "Ratol"],
          ["Siam", "Joy", "Araf", "Roy"]]

# same we can make 2d tuples
group2 = (("Arman", "Saief", "Hasib", "Sabbir"),
          ("Rahul", "Bornil", "Sabit", "Riyad"),
          ("Rakib", "Pappu", "Ajmain", "Ratol"),
          ("Siam", "Joy", "Araf", "Roy"))

# 2d sets is not possible
# note: we cannot use set as an set element, so 2d set is not possible

# print(groups)
# [['Arman', 'Saief', 'Hasib', 'Sabbir'], ['Rahul', 'Bornil', 'Sabit', 'Riyad'], ['Rakib', 'Pappu', 'Ajmain', 'Ratol'], ['Siam', 'Joy', 'Araf', 'Roy']]

print("For 2D list")
i1 = 0
for group in groups:
    # print(group)
    # this will print every group by new line
    i1+=1
    print(f"Group Number {i1}:")
    i2  = 0
    for man in group:
        i2+=1
        print(f"  {i2}. {man}")
        
        # Group Number 1:
        #   1. Arman
        #   2. Saief
        #   3. Hasib
        #   4. Sabbir
        # Group Number 2:
        #   1. Rahul
        #   2. Bornil
        #   3. Sabit
        #   4. Riyad
        # Group Number 3:
        #   1. Rakib
        #   2. Pappu
        #   3. Ajmain
        #   4. Ratol
        # Group Number 4:
        #   1. Siam
        #   2. Joy
        #   3. Araf
        #   4. Roy
        
print()
print("For 2D tuples")
i1 = 0
# for 2d tuples
for group in group2:
    # print(group)
    # this will print every group by new line
    i1+=1
    print(f"Group Number {i1}:")
    i2  = 0
    for man in group:
        i2+=1
        print(f"  {i2}. {man}")
        
# we should use 2D list or 2D tuple, but tuples are faster than list!
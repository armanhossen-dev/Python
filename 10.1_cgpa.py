print("-------------CGPA Calculator-------------")
while True:
    hmc = int(input(("How Many Courses: ")))
    if hmc < 0:
        print("Course Number cann't be negative!, Try again")
    else:
        break

i = 0
sumA = 0
totalCredit = 0
while True:
    i += 1
    # subjectCredit = float(input(f"{i}. Enter Credit: "))
    # A = float(input("Grade Point: "))
    subjectCredit, A = map(float, input(f"{i}. Enter Credit and Grade Point: ").split()) # 2. Enter Credit and Grade Point: 1.5 4
    
    totalCredit += subjectCredit
    sumA += (A*subjectCredit)
    
    if i == hmc:
        break

res = sumA/totalCredit
res = round(res, 2)

print(f"Total Credit: {totalCredit} SGPA: {res}")
print("-----------------------------------------")

# -------------CGPA Calculator-------------
# How Many Courses: 5
# 1. Enter Credit and Grade Point: 3 3.25
# 2. Enter Credit and Grade Point: 1.5 4
# 3. Enter Credit and Grade Point: 3 3
# 4. Enter Credit and Grade Point: 1.5 3.5
# 5. Enter Credit and Grade Point: 3 3
# Total Credit: 12.0 SGPA: 3.25
# -----------------------------------------
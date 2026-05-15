# Python Quiz Game
questions = ("1. How many elements are there in the periodic table?",
             "2. Which animal lays the largest eggs?",
             "3. What is the most abundant gas in Earth's atmosphere?",
             "4. How many bones are in the human body?",
             "5. Which planet in solar system is the hottest?")

options = (("A. 108 ", "B. 101", "C. 118", "D. 75 "), # c
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"), # d
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"), # a
           ("A. 206", "B. 207", "C. 200", "D. 202"), # a
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")) # b

answers = ("c", "d", "a", "a", "b")
guesses = []
score = 0

# Refined Loop, it gives index and item at the same time
for index, question in enumerate(questions):
    print("---------------------Quesetions------------------------------")
    print(question)
    for op in options[index]:
        print(op)

    g = input("Enter your Ans (A, B, C,  D): ").lower()
    guesses.append(g)
    
    if g == answers[index]:
        score+=1
        print("Correct Answer!")
    else:
        print(f"Incorrect! {answers[index]} was the correct answer.")

print("-----------------------Result----------------------------")

print("Guesses: ", end=" ")
for ans in guesses:
    print(ans, end=" ")
print()

print("Answers: ", end=" ")
for ans in answers:
    print(ans, end=" ")
print()

print(f"Your final Score is {score}/{len(questions)}") # number of question - len(questions)
print(f"Your grade: {(score/len(questions)) * 100}%") # score percentage

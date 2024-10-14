#Created a variable that will store all the correct points. Initialized at zero
quiz_score = 0

#Created a question for the user to answer
print("(John Matthew Arroyo)1. Who is Luffy's grandfather in One Piece?\n A. Garp\n B. Smoker\n C. Crocodile\n D. Dragon\n")

#Created a variable that will let the user input their answer
player_answer = input("Enter your answer: ")

#If statements to check if the user inputted the correct answer
if player_answer == "a" or player_answer == "A":
    print("Correct Answer!\n")
    quiz_score += 1
else:
    print("Incorrect Answer. The correct answer is A\n")
    
#THE REST OF THE QUESTIONS FOLLOW THE SAME PATTERN   
print("(John Matthew Arroyo)2. Who is Luffy's vice captain?\n A. Ussop\n B. Mihawk\n C. Zoro\n D. Nami\n")

player_answer = input("Enter your answer: ")

if player_answer == "c" or player_answer == "C":
    print("Correct Answer!\n")
    quiz_score += 1
else:
    print("Incorrect Answer. The correct answer is C\n")
    
print("(John Matthew Arroyo)3. Who owns the treasure One Piece?\n A. Gold Roger\n B. Luffy\n C. Shiki\n D. No one\n")

player_answer = input("Enter your answer: ")

if player_answer == "d" or player_answer == "D":
    print("Correct Answer!\n")
    quiz_score += 1
else:
    print("Incorrect Answer. The correct answer is D\n")
    

    

    




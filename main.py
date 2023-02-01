import random #Randomizes the values in the list.
numbers = [1,2,3,4,5] #List containing values that will be chosen at random for the addition questions.
def math(numbers): #Function with 'numbers' as the parameter. 
  print("Hello! Welcome to this addition math game! Good luck!") #States what the program will be
  while True: #Loop to ask multiple questions if the user chooses to.
      computer = random.choice(numbers) #Randomizes the chosen numbers from the list 'numbers'.
      print("Question:", computer, "+" , computer) #Prints the question of the randomized number(computer) + the randomized number(computer).
      answer = int(input("What is the answer?" )) #Asks the user what they think the answer is.
      if answer == computer + computer: #If the user's 'answer", according to the computer, equals the randomized number(computer) + the randomized number(computer) it will either print 'correct' or incorrect.
        print("Correct!") # If 'answer' is correct, prints 'correct'.
      else: 
        print("Incorrect") # If 'answer' is incorrect, prints 'incorrect'.
      Again = input("Do you want to play again? (yes/no) ") #Asks the user if they want to play again.
      if Again != "yes": #If users does not say 'yes' it will print 'goodbye' and end the loop/program. If user says 'yes' the loop will repeat and print another randomized question.
        print("Goodbye!")
        exit()
math(numbers) #Calls the function.
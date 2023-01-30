import random 
numbers = [1,2,3,4,5]
# print(numbers[0], "+" ,numbers[1])
def math(numbers):
  print("Hello! Welcome to this addition math game! Good luck!")
  ready = input("Ready?")
  if ready != "yes":
    exit()
  while True:
      computer = random.choice(numbers)
      print("Question:", computer, "+" , computer)
      answer = int(input("What is the answer?" ))
      if answer == computer + computer:
        print("Correct!")
      else: 
        print("WRONG")
      Again = input("Do you want to play again? (yes or no) ")
      if Again != "yes":
        print("Goodbye!")
        exit()
math(numbers)
  
  # computer = random.choice(numbers)
  # print(computer, "+" , computer)
  
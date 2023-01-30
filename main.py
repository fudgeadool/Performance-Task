import random 
numbers = [1,2,3,4,5]
# print(numbers[0], "+" ,numbers[1])
def math(numbers):
  print("Hello! Welcome to this math game! You have to get 3 questions correct to win! Good luck!")
  computer = random.choice(numbers)
  print("Question #1:", computer, "+" , computer)
  ok =input("What is the answer?" )
  if int == computer + computer:
    print("Correct!")
  else: 
    print("WRONG")


math(numbers)

# computer = random.choice(numbers)
# print(computer, "+" , computer)

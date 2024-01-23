import random

print('lets play')
print('stone,paper,scissor')
user = input()
user = user.lower()

choice = ["stone", "paper", "scissor"]
computer = random.choice(choice)
print(computer)

if user == 'stone' and computer == 'paper':
    print("you lose!")
elif user == 'stone' and computer == 'scissor':
    print("you win!")
elif user == 'scissor' and computer == 'paper':
    print("you win!")
elif user == 'scissor' and computer == 'stone':
    print("you lose!")
elif user == 'paper' and computer == 'scissor':
    print("you lose!")
elif user == 'paper' and computer == 'stone':
    print("you win!")
elif user == computer:
    print("it's tie")
else:
    print("invalid input")

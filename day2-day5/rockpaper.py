# (r,p,s)
# (r,p,s)

import random


possibleChoice = ["rock","paper","scissor"]
userChoice= input("Eneter your choice (rock,paper,scissor):")
computerChoice = random.choice(possibleChoice)
print(f"your choice : {userChoice} \n")
print(f"Computer choice is {computerChoice}")

if userChoice == computerChoice:
    print("tie!!!!!")
elif userChoice == "rock":
    if computerChoice == "Scissor":
        print("Rock smashes scissor ! you win")
    else:
        print("computer choses paper and we lost")
elif userChoice == "paper":
    if computerChoice == "rock":
            print("Paper covers rock! You win!")
    else:
            print("Scissors cuts paper! You lose.")
elif userChoice == "scissors":
    if computerChoice == "paper":
            print("Scissors cuts paper! You win!")
else:
     print("Rock smashes scissors! You lose.")

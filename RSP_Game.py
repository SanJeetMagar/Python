import random
while True: 
    play = input("Do you want to play Rock, Scissor, Paper (Y/N)? ").lower()
    if play == "y":
            break
    elif play == "n":
        print("Thank you for your response") 
        exit()
    else:
        print("Invalid input")
while True:
                
    choice = input("Pick between Rock, Scissor, Paper: ").capitalize()
    computer_choice = random.choice(["Rock", "Scissor", "Paper"])   
    print(f"Computer choice is {computer_choice}")
    if choice == computer_choice:
            print("Its draw")
    elif (choice == "Rock" and computer_choice == "Paper") or (choice == "Paper" and computer_choice == "Scissor") or (choice == "Scissor" and computer_choice == "Rock"):
            print("You loss")
    elif (choice == "Rock" and computer_choice == "Scissor") or (choice == "Paper" and computer_choice == "Rock") or (choice == "Scissor" and computer_choice == "Paper"):
         print("You win")
    else:
         print("Invalid input")
    ask = input("Do you want to continue Y/N? ").lower()
    if ask == "y":
        continue
    elif ask == "n":
         break
    else:
         print("Invalid input")
   

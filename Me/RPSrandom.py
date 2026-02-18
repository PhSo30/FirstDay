import random
choice = ["rock","paper","scissors"]
w=l=0
while w<3 and l<3:
    while(u:=input("Enter rock, paper, or scissors: ").lower()) not in choice:
        print("Invalid choice. Please try again.")
    c=random.choice(choice)
    print(f"Computer: {c}")
    r="Tie!" if u==c else "You win!" if (u,c) in [("rock","scissors"),("paper","rock"),("scissors","paper")] else "You lose!"
    print(r)
    w+=r=="You win!"
    l+=r=="You lose!"
print("You win the game!" if w-l>0 else "You lose the game!")
print(f"You {w} - Computer {l}")
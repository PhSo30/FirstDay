import random

Lucky_num = random.randint(1, 11)
print(Lucky_num)
for k in range(1, 4):
    Guess_num = int(input("Enter your guess number: "))

    if Guess_num == Lucky_num:
        print("Correct")
        break
    else:
        print("Incorrect")
    if k == 3:
        print("You loss")
        break

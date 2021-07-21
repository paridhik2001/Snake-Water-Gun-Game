# Snake Water Gun Game

import random
i=0
cnt1=0
cnt2=0
while(i<8):
    print()
    i=i+1
    print("Round No. ",i)
    lst = ["S", "W", "G"]
    choice_comp = random.choice(lst)
    print("Enter your choice S(Snake), W(Water), G(Gun)")
    choice = input()
    if choice=="S" and choice_comp=="W":
        cnt1=cnt1+1
    elif choice=="W" and choice_comp=="S":
        cnt2=cnt2+1
    elif choice == "G" and choice_comp == "S":
        cnt1 = cnt1 + 1
    elif choice == "S" and choice_comp == "G":
        cnt2 = cnt2 + 1
    elif choice == "W" and choice_comp == "G":
        cnt1=cnt1+1
    elif choice == "G" and choice_comp == "W":
        cnt2=cnt2+1
    print("Computer's Choice : ",choice_comp)
    print("Your Score : ",cnt1)
    print("Computer's Score : ", cnt2)

if cnt1>cnt2:
    print("You Won")
elif cnt1==cnt2:
    print("Draw")
else:
    print("You Lost")


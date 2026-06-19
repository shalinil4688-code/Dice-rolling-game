import random
while True:
    choice=input("roll the dice? (y/n):")
    if choice=="y":
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print("(",dice1,",",dice2,")")
    else:
        print("thanks for playing")
        break
    

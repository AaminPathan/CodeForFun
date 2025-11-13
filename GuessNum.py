import random

print("WELCOME TO NUMBER GUESS")
print("Enter number betn 1-100")

Guess=random.randint(1,100)
attemt=0
while True:
    num=int(input("ENTER YOUR CHOICE NUMBER:"))
    attemt +=1

    if num==Guess:
        print("YOU WON")
        print(f"Number was {Guess}")
        print(f"Numbers of attemts you took:{attemt} ")
        break   
    elif num>Guess:
        print("come back")     
    elif num<Guess:
        print("go furthur")  
    
import random
# computer=random.randint(10,100)
# a=random.randint(1,100)
# b=random.randint(1,100)

print("Guess the  correct number to win the game😊")
print("Lets check your calculation power😜😜")

# reversenum=int(str(y)[::-1])
for i in range(1,11):
    computer=random.randint(10,100)
    a=random.randint(1,100)
    b=random.randint(1,100)

    
    print(f"Add {a}={computer+a}")
    y=computer+a
    reversenum=int(str(y)[::-1])
    print(f"Reverse the digit and get:{reversenum}")
    k=print(f"subtract{b}:{reversenum-b}")

    yourguess=int(input("Enter your guess:"))
    if(yourguess==computer):
        print("Wow😍you have cracked it")

    else:
        print("Wrong!The correct answer is",computer)

print("GAME OVER")
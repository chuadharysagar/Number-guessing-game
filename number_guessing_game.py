import random
randomno= random.randint(1,100)
nguesses=0
userguess=None
print(random)

while(userguess != randomno):
    userguess=int(input("Enter your guess: "))
    if(userguess==randomno):
        print("you guesssed it right !! ")
    else:
        if(userguess>randomno):
            print("you guessed it wron ! enter SMALLER number")
        else:
            print("you guessed it wrong ! enter LARGER number")
    nguesses+=1
print(f"you guessed it in {nguesses} attempts!!")
# with open("gamehicore.txt","w") as f:
#     f.write(nguesses)
with open("gamehiscore.txt","r") as f:
    data=f.read()
    print(data)
if(nguesses<data):
    with open ("game hiscore.txt","w") as f:
        f.write(str(nguesses))

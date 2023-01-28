import random
print("Let's guess the computer number between 1 to 10!")
y= input("Want to play the game?'Yes' or 'No' ")
score=0
while y=="Yes":
    t = random.randint(1,10)
    #print(t)
    a= int(input("Guess the number between 1 to 10: "))
    if t==a:
        print("You won!")
        print("Computer Number is : "+str(t))
        score += 1
    else:
        print("You lost!")
        print("Computer Number is : "+str(t))
    y= input("Want to play the game?'Yes' or 'No' ")
if y!="Yes":
    print("Your score is "+str(score))
    if score <=0:
        print("You are loser!You can even win robot!")
    
    

    

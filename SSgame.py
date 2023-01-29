print("Our game has only two rules!!")
print("1.Your age must be over 14")
print("2.You should smart enough to play this game 😒")
name = input ("What is your name?: ")
age = int(input ("What's your age!: "))
password=input("Give the password: ")
if age >=14:
   print("You can play this game!!")
   print("Welcome 🤗 "+ name)
   shopo= input ("What do you want to give a name for shop owner!😀")
   print ("You gave the shop owner name -"+shopo)
   robot=input ("How about to your robot assistant?")
   print ("Ok!🤖"+robot)
   a=input ("Do you want to enter the room?: ")
   if a=="Yes" or a=="Y" or a=="yes" or a=="y":
      print ("You entered the room room!!")
      print ("Now go to upstairs 😊")
      print("You need to do upstairs.And there are two ladders.One of them is a fake ladder")
      print("Hint: Most of people are ___handed.")
      b = input("'L' For left ladder and 'R' For right ladder: ")
      
      if b == "R":
         print("You arrived upstair.")
      while b != "R" :
         print("You are wrong.You can try again.")
         b = input("'L' For left ladder and 'R' For right ladder: ")
         print("You arrived upstair.")
         
      input("Welcome to the digital Sweet Shop!! ")
      print("I'm "+robot)
      input("You have been invited to take part in a competition in the shop.")
      input("You must find the chocolate room. And you will be asked a question!! ")
      print("If you get it right you will receive letter which are part of a password and a clue of where it is.")
      input("If you are wrong, your jounary will end!! You only have one chance!YOU CANNOT MAKE MISTAKE!")
      a=input("What is the founder of tesla? ")
      if a =="Elon Mask":
       print("You are right!")
       print("It is a last room in this digital Sweet shop. There are 4 letters.The first two letters are A-X.")
      elif a !="Elon Mask":
       print("You are wrong. You lose the chance to win a competition")
       exit()
       
      input("In this room, there is a host. She will explain the rules. ")
      input("Hi I am lisa. I am a host of this room. ")
      input("You have been invited to take part in a competition in the shop. ")
      print("You need to answer two questions. To get the two last number of the password and to open the treature box.")
      print("Will you do it? ")
      b=input("What is the most popular language in the world??")
      if b =="English":
       print("You are right!And the last Question.")
      elif b !="English":
       print("You are wrong. You lose the chance to win a competition")
       exit()

      c=int(input("What time is the first time python release? "))

      if c ==1991:
       print("You are right! The two last numbers of the password are 4-1")
      elif c !=1991:
       print("You are wrong. You lose the chance to win a competition")
       exit()

      print("Now you can open the treature box!!")
      d=input("What is the password of the treature box? ")

      if d =="A-X-4-1":
       print("You opened the treature box.")
      elif d !="A-X-4-1":
         print("Wrong password! You are Loser.But You can try again loser!")
         exit()
            

      print("In the treature box which contains a year's supply of all your favourite sweets")
      print("You will meet two people one is the sweet owner who wants to steal the password so he can keep the sweets")
      print("###################################################################")
      #Meet with Owner
      chocolate = 3
      print("HI,I am shop owner, "+shopo)
      input("I am glate.You win first level,bot level ")
      print("Now you have 3 chocolate bars because you won")
      print("Chocolate bar is equal life.When you lost all chocolate bar,you will lose.(Game over)")
      print("If you win this game you will have unlimited chocolate.")
      n=input("Do you agree? and Will you do it?(Yes or No)")
      if n=="Yes":
        print("You are brave.")
        print("I will ask 2 questions and if you correct all, you will become winner.")
        j=input("What is the password? Type(A or B or C)Hint: A:A-X-1-4 "+"B:"+password+" C:A-X-4-1 ")
        if j=="C":
            print("You are right.")
            v=int(input("2+4x-10=0 x=?? "))
            if v==2:
                print("You are right. YOu become a true winner.")
                print("You have unlimited chocolate.")
            while v!=2:
                print("You are wrong.")
                chocolate-=1
                print("You have "+ str(chocolate)+ "chocolate.")
                if chocolate<0:
                    print('YOU lost your all chocolates.GAME OVER')
                    exit()
                v=int(input("2+4x-10=0 x=?? "))
                if v==2:
                    print("You are right. YOu become a true winner.")
                    print("You have unlimited chocolate.")
        while j!="C":
            print("You are wrong.")
            chocolate-=1
            print("You have "+ str(chocolate)+ "chocolate.")
            if chocolate<0:
                print('YOU lost your all chocolates.GAME OVER')
                exit()
            j=input("What is the password? Type(A or B or C) Hint: A:A-X-1-4 B:A-4-X-1 C:A-X-4-1 ")
            if j=="C":
                print("You are right.")
                v=int(input("2+4x-10=0 x=?? "))
                if v==2:
                    print("You are right. YOu become a true winner.")
                    print("You have unlimited chocolate.")
                  
      elif n=="No":
        print("You are loser.")
      while n!="Yes":
        print("Type carefully No or Yes")
        n=input("Do you agree? and Will you do it?(Yes or No)")
        if n=="Yes":
            print("You are brave.")
            print("I will ask 2 questions and if you correct all, you will become winner.")
            j=input("What is the password? Type(A or B or C)Hint: A:A-X-1-4 "+"B:"+password+" C:A-X-4-1 ")
            if j=="C":
                    print("You are right.")
                    v=int(input("2+4x-10=0 x=?? "))
                    if v==2:
                        print("You are right. YOu become a true winner.")
                        print("You have unlimited chocolate.")
                    while v!=2:
                        print("You are wrong.")
                        chocolate-=1
                        print("You have "+ str(chocolate)+ "chocolate.")
                        if chocolate<0:
                         print('YOU lost your all chocolates.GAME OVER')
                         exit()
                        v=int(input("2+4x-10=0 x=?? "))
                        if v==2:
                            print("You are right. YOu become a true winner.")
                            print("You have unlimited chocolate.")
            while j!="C":
                print("You are wrong.")
                chocolate-=1
                print("You have "+ str(chocolate)+ "chocolate.")
                if chocolate<0:
                 print('YOU lost your all chocolates.GAME OVER')
                 exit()
                j=input("What is the password? Type(A or B or C) Hint: A:A-X-1-4 B:A-4-X-1 C:A-X-4-1 ")
                if j=="C":
                 print("You are right.")
                 v=int(input("2+4x-10=0 x=?? "))
                 if v==2:
                    print("You are right. YOu become a true winner.")
                    print("You have unlimited chocolate.")
   else:
        print ("Ok!You can come back anytime 😉")
else:
   print("Sorry! You are too young to play this game")

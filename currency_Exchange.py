#program
# I want a calculator to calculator dollars to Myanmar Kyats
# or kyats to dollars
ans=input("What do you want to calculate? Dollars or Kyats? ") #ask the user which one he or she wants to use

if ans=="Dollars":                                             # This is 
   dollars= int(input("Enter your dollars amounts: "))         # If user choose dollars
   kyats=dollars*3000                                          # will run this code!
   print("You have " + str(kyats) + " kyats.")                 # !!!!!!!!

elif ans=="Kyats":                                             # This is
   kyats= int(input("Enter your kyats amounts: "))             # If user choose dollars
   dollars= kyats/3000                                         # will run this code!
   print("You have " + str(dollars) + " Dollars")              # !!!!!!!!

else:                                                          # if it is not both situation
    print("You have syntax error in Dollars or Kyats ")        # will run this code!
    print("Please type carefully!!")                           # !!!!!!!!

#program

#loop4
times = int(input("Which times table do you want to see"))
number=0
while number <=12:
    result= times * number
    print(str(times)+"*"+str(number)+"="+str(result))
    number = number+1

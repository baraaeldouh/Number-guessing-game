import random
print("welcome to the number guessing game")
secret_number=random.randint(1,10)
attembt=0
while True:
    guess=int(input("enter number"))
    attembt+=1

    if guess==secret_number:
        print("correct")
        break
    elif guess>secret_number:
        print("please try again")
    else:
         print("please try again")




    

import random

limit = int(input("Enter the upper limit upto which you want to guess : "))

guess_no = random.randint(1,limit)
attempts = 1

while True:
    check_no = int(input(f"Enter the number to guess between 1 to {limit} :"))
    if( check_no == guess_no ):
        print("Congrats !! you guessed the answer ")
        break
    elif ( check_no > guess_no ):
        print("go lower")
    else:
        print("go higher")
    
    attempts+=1


print(f"You took {attempts} attempts to guess the correct answer ")
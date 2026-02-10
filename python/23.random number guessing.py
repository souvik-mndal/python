import random

start = int(input("Enter the starting point : "))
end = int(input("Enter the ending point : "))

chance = 3
ans = random.randint(start,end)

while( chance ):
    guess = int(input("Enter the number you are guessing : "))
    if( guess > ans ):
        print("Think lesser")
    elif( guess < ans ):
        print("Think bigger")
    else:
        print("You have guessed the number which is ",ans)
        break
    chance-=1
else:
    print("your all the chances are over , GAME OVER")
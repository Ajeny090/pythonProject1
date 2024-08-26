import random


print("Welcome of the game to guess a number!!!")
user = input("Do you want to play the game?Yes or no: ").lower()
num = random.randint(0,100)
if user == "yes":
    while True:
        guess = int(input("Enter a number: "))
        if guess < num:
            print("The number is low.")
        elif guess > num:
            print("The number is above.")
        elif guess == num:
            print("Congratulation, you won")
else:
    print("Thank you, try another time.")
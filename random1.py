import random

def guess(x):
    random_number = random.randint(1,x)
    guess=0
    while guess != random_number:
        guess =int(input(f"Guess your number between 1 to {x} :"))
        if guess<random_number:
            print ("your guess number is low")

        elif guess>random_number:
            print("your guess number is high ")

    else:
        print (f"aah! you guessed random number is {random_number} is correct")


def computer_guess(x):
    low = 1
    high = x
    feebback = " "
    guess = ""
    while guess != "C":

        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feebback = input(f" if {guess} is high (H),low (L) or correct(C) :").upper()
        if feebback == "H":
            high = guess-1

        elif feebback == "L":
            low = guess + 1 

        elif feebback=="C":
            print (F"you are win your guess {guess} is correct")
            break
            
        else:
            print ("i am not understand what you type")
            break
    

computer_guess(100)

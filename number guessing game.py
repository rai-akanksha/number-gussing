import random
def guess_number():
    random_number = random.randint(1,20)
    player_name = input("Enter Your Name: ")
    confirm_play = input("Would you like to start the game? (Enter yes/no): ")
    attempts = 0

    while confirm_play.lower() == "yes":

        guess = int(input("Guess any number between 1 and 20: "))

        if guess < 1 or guess > 20:
            print("Please guess any number in the Range.")

        elif guess == random_number:
            print("Conguratulations ", player_name, 'You Won!')
            attempts +=1
            print("It took you ", attempts, "attempts to win this Game")
            break

        elif guess > random_number:
            print("HINT: try smaller number")
            attempts +=1
        
        elif guess < random_number:
            print("HINt: try larger number")
            attempts +=1


    else:
        print("Thanks ", player_name, "for your Time.")
guess_number()
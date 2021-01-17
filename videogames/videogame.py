import random

def run():
    aleatory_number = random.randint(1, 100)

    user_lives = int(input("How many lives do you want to have in this game?: "))
    user_lives -= 1
    user_number = int(input("Choose a number between 1 and 100: "))
    
    while user_number != aleatory_number:

        if user_number < aleatory_number and user_lives > 0:
            user_lives -= 1
            user_number = int(input("It's bigger. Choose another number: "))

        elif user_number > aleatory_number and user_lives > 0: 
            user_number = int(input("It's lower. Choose another number: "))
            user_lives -= 1
            
        if user_lives == 0:
            user_number == aleatory_number
            break

    if user_lives > 1 and user_number == aleatory_number:
        print("You won!!!")
    else:
        print(f"You lost, try again!!!, the number was {aleatory_number}")


if __name__ == '__main__':
    run()
from random import randint
#choosing a random number between 1 and 100
number = randint(1, 100)
print(number)

def game():
    EASY = 10
    HARD = 5
    def check_difficulty():
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': easy")
        if difficulty == 'easy':
            return 10
        elif difficulty == 'hard':
            return 5
    turns = check_difficulty()

    user_guess = int(input("Make a guess: "))
    def check_number():
        if user_guess > number:
            print("Too high")
            turns -1
        elif user_guess < number:
            print("Too low")
            turns -1    


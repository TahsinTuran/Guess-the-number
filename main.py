import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)

number = random.randint(1, 100)

easy_hard = input("Choose a difficulty. Type 'easy' or 'hard': ")

if easy_hard == "easy":
    chances = 10
elif easy_hard == "hard":
    chances = 5 
else:
    print("Enter from the options. Type 'easy' or 'hard': ")
def input_guess():
        global chances
        print(f"You have {chances} attempts remaining to guess the number. ")
        
        chances -= 1
        
def number_check(guess):
    global is_game_over
    global number
    if guess == number:
        print(f"You got it! The answer was {number}.")
        is_game_over = True
    elif chances == 0:
        print("You've run out of guesses, you lose.")
        is_game_over = True    
    elif guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
is_game_over = False
while not is_game_over:  
    input_guess()
    make_a_guess = int(input("Make a guess :"))
    number_check(make_a_guess)   
def clear() -> None:
    """Clear the terminal."""
    print("\033[H\033[2J", end="", flush=True)




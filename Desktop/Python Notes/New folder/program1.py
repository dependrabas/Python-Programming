import random

def guess_number():
    
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        
        guess = input("Enter your guess (or 'exit' to end the game): ")

        
        if guess.lower() == 'exit':
            print(f"The secret number was {secret_number}. Better luck next time!")
            break

        try:
           
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

  
        attempts += 1

       
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    guess_number()

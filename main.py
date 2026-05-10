import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    
    # Difficulty selection
    print("\nChoose Difficulty:")
    print("1. Easy (1–50, 10 attempts)")
    print("2. Medium (1–100, 7 attempts)")
    print("3. Hard (1–200, 5 attempts)")
    
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        max_num = 50
        attempts = 10
    elif choice == '2':
        max_num = 100
        attempts = 7
    elif choice == '3':
        max_num = 200
        attempts = 5
    else:
        print("Invalid choice. Defaulting to Medium.")
        max_num = 100
        attempts = 7

    number = random.randint(1, max_num)

    print(f"\nI have selected a number between 1 and {max_num}.")
    print(f"You have {attempts} attempts to guess it.\n")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        if guess < number:
            print("📉 Too low!")
        elif guess > number:
            print("📈 Too high!")
        else:
            print(f"🎉 Correct! You guessed it in {attempt} attempts.")
            break
    else:
        print(f"😢 Game Over! The number was {number}.")

    # Replay option
    replay = input("\nDo you want to play again? (y/n): ").lower()
    if replay == 'y':
        number_guessing_game()
    else:
        print("👋 Thanks for playing!")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
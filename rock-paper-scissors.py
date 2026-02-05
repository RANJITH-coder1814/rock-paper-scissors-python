import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "user"
    else:
        return "computer"

def main():
    user_score = 0
    computer_score = 0

    print("===== Rock Paper Scissors Game =====")

    while True:
        user_choice = input("\nChoose rock, paper, or scissors: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(user_choice, computer_choice)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win! ")
            user_score += 1
        else:
            print("Computer wins! ")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing! ")
            break

if __name__ == "__main__":
    main()

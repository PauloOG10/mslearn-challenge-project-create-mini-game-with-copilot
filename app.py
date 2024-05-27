import random

def get_user_input():
    user_input = str(input("Enter your option: ")).lower()
    return user_input

# Write a function that generates a random number between 0 and 2
def generate_random_number():
    return random.randint(0, 2)

def main(user_score=0, computer_score=0):
    valid_options = ["rock", "paper", "scissors"]
    user_input = get_user_input()
    if user_input not in valid_options:
        print("Invalid option, you must choose between rock, paper or scissors")
    else:
        computer_input = valid_options[generate_random_number()]
        if user_input == computer_input:
            print(f"Both players selected {user_input}. It's a tie!")
        elif user_input == "rock":
            if computer_input == "scissors":
                print("Rock smashes scissors! You win!")
                user_score += 1
            else:
                print("Paper covers rock! You lose.")
                computer_score += 1
        elif user_input == "paper":
            if computer_input == "rock":
                print("Paper covers rock! You win!")
                user_score += 1
            else:
                print("Scissors cuts paper! You lose.")
                computer_score += 1
        elif user_input == "scissors":
            if computer_input == "paper":
                print("Scissors cuts paper! You win!")
                user_score += 1
            else:
                print("Rock smashes scissors! You lose.")
                computer_score += 1

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        main(user_score, computer_score)
    else:
        print(f"Final User score: {user_score}")
        print(f"Final Computer score: {computer_score}")
        print("Goodbye!")

if __name__ == "__main__":
    main()


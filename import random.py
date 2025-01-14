import random

def get_user_choice():
    user_input = input("Kérlek válassz (kő, papír, olló): ").lower()
    if user_input in ['kő', 'papír', 'olló']:
        return user_input
    else:
        print("Hibás válasz, próbáld újra!")
        return get_user_choice()

def get_computer_choice():
    return random.choice(['kő', 'papír', 'olló'])
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Döntetlen!"
    elif (user_choice == 'kő' and computer_choice == 'olló') or \
         (user_choice == 'olló' and computer_choice == 'papír') or \
         (user_choice == 'papír' and computer_choice == 'kő'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"A te választásod: {user_choice}")
    print(f"A gép választása: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
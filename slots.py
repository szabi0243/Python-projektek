import random

def spin_row():
    symbols = ["🍒", "💰", "🍊", "🍋", "🍉"]

    return [random.choice(symbols) for _ in range(3)]
def print_row(row):
    print("**********************************")
    print(" | ".join(row))
    print("**********************************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "💰":
            return bet * 20
        elif row[0] == "🍊":
            return bet * 6
        elif row[0] == "🍋":
            return bet * 9
        elif row[0] == "🍉":
            return bet * 15
        print("JACKPOT! 🎉")
    return 0

def main():
    balance = 100

    print("**********************************")
    print("Welcome to the slot machine!")
    print("Symbols: 🍒  💰  🍊  🍋   🍉")
    print("**********************************")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount:")

        if not bet.isdigit():
            print("Please enter a valid number!")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds!")
            continue

        if bet <= 0:
            print("Invalid bet amount!")
            continue

        balance -= bet

        row = spin_row()
        print("spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print("You lost!")

        balance += payout

        play_again = input("Do you want to play again? (y/n): ")

        if play_again != "y":
            break
    print("**********************************")
    print(f"Game over! Your final balance is ${balance}")
    print("**********************************")

if __name__ == "__main__":
    main()
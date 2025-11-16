import random
import time

def flip_coin():
    return random.choice(['Heads', 'Tails'])

def rounds(first_player, second_player):
    print("  New Round  ")

    first_player_choice=input(f" {first_player} Heads or Tails").strip().capitalize()

    second_player_choice = "Tails" if first_player_choice == "Heads" else "Heads"
    print(f" {second_player} gets {second_player_choice}")

    print("\nFlipping the coin...")
    time.sleep(1)
    result = flip_coin()
    print(f"The coin landed on: {result}")

    if result == first_player_choice:
        print(f"Congratulations, {first_player} wins!")
        return first_player_choice

    else:
        print(f"Congratulations, {second_player} wins!")
        return second_player

def main():
    first_player = input("what is your name?").strip().capitalize()
    second_player = input("what is your name?").strip().capitalize()
    print(f"Welcome to Flipping Coin {first_player} and {second_player}!")

    scores={first_player:0, second_player:0}
    while True:
        winner=rounds(first_player, second_player)
        scores[winner] += 1

        print(f"\nCurrent Scores:")
        print(f"{first_player}: {scores[first_player]} | {second_player}: {scores[second_player]}")
        #Do you want play again?
        again=input("Would you like to play again? (Yes/No)").strip().capitalize()
        if again!="Yes":
            print("Thank you for playing!")
            print("Your final scores:")
            print(f"{first_player}  {scores[first_player]} | {second_player}: {scores[second_player]}")
            break

if __name__=="__main__":
    main()
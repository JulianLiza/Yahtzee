from player import Player
import Check_input

def take_turn(player):
    """Handles a single turn for the player."""
    player.roll_dice()  # Roll the dice
    print(player)  # Display dice values

    # Check for win conditions
    if player.has_three_of_a_kind():
        print("You got 3 of a kind!")
    elif player.has_series():
        print("You got a series of 3!")
    elif player.has_pair():
        print("You got a pair!")
    else:
        print("Aww. Too Bad.")

    # Display updated score
    print(f"Score = {player.points}")

def main():
    """Main function that runs the game loop."""
    print("-Yahtzee-")
    player = Player()  # Create a Player object

    while True:
        take_turn(player)  # Play one turn
        if not Check_input.get_yes_no("Play again? (Y/N): "):  # Ask to continue
            break  # Exit loop if the user says no

    print("Game Over.")
    print(f"Final Score = {player.points}")

if __name__ == "__main__":
    main()
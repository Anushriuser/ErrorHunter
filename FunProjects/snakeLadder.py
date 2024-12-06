import random

def snake_and_ladder():
    position = 0
    for _ in range(100):  # Limit the number of turns to 100
        dice = random.randint(1, 6)
        if position + dice > 100:
            continue  # Skip the move if it overshoots 100
        position += dice
        if position == 50:  # Climbing a ladder
            position = 75
            print(f"Climbed the ladder to Position: {position}")
        elif position == 25:  # Snake bite
            position = 10
            print(f"Snake bite! Moved to Position: {position}")
        else:
            print(f"Position: {position}")

        if position == 100:
            print("Congratulations! You have reached Position 100.")
            break

snake_and_ladder()
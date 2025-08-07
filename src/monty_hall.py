import random
from typing import Tuple


def monty_hall_game(switch_door: bool = True) -> bool:
    """Simulate a Monty Hall game for a single round.

    :param switch_door: Whether to switch the chosen door after one is revealed, defaults to True
    :return: Whether the player won the car
    """
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)

    init_choice = random.choice(range(3))

    if switch_door:
        revealable_doors = [i for i in range(3) if i != init_choice and doors[i] != 'car']
        revealed_door = random.choice(revealable_doors)
        final_choice = [i for i in range(3) if i != init_choice and i != revealed_door][0]
    else:
        final_choice = init_choice

    return doors[final_choice] == 'car'


def game_simulator (num_trials: int = 100) -> Tuple[float, float]:
    """Simulate the Monty Hall game for a given number of trials.

    :param num_trials: Number of trials to run, defaults to 100
    :return: Win rates for switching and not switching
    """
    num_wins_with_switching = sum([monty_hall_game(True) for _ in range(num_trials)])
    num_wins_without_switching = sum([monty_hall_game(False) for _ in range(num_trials)])

    return num_wins_with_switching, num_wins_without_switching


if __name__ == "__main__":
    num_trials = 100000
    win_rate_with_switching, win_rate_without_switching = game_simulator(num_trials)
    print(f"Win rate with switching: {win_rate_with_switching:.4%}")
    print(f"Win rate without switching: {win_rate_without_switching:.4%}")

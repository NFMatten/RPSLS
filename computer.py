from player import Player
from random import choice

class Computer(Player):
    def __init__(self):
        super().__init__()

    def random_gesture_selection(self):
        """
        Purpose: Randomly selects gesture from list
        """
        # computer_selection = choice.LIST

    def computer_scoring(self):
        """
        Purpose: If computer wins round, +1 to their score
        """
        
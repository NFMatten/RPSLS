from player import Player
from random import choice

class Computer(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def choose_gesture(self):
        """
        Purpose: Randomly selects gesture from list
        """
        computer_selection = choice(self.gestures)
        print(f'Computer chose {computer_selection}')
        self.chosen_gesture = computer_selection


from player import Player
from random import choice

class Computer(Player):
    def __init__(self):
        super().__init__('ricky')

    def choose_gesture(self):
        """
        Purpose: Randomly selects gesture from list
        """
        computer_selection = choice(self.gestures)
        print(computer_selection)
        return(computer_selection)


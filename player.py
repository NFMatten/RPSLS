from operator import imod
from gesture import Gesture
from rock import Rock
from paper import Paper
from scissors import Scissors
from lizard import Lizard
from spock import Spock

class Player:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.gestures = [Rock(), Paper(), Scissors(), Lizard(), Spock()]
        self.selected_gesture = None

    def choose_gesture(self):
        """
        Purpose: Chooses gesture by way of polymorphism
        """
        pass
   
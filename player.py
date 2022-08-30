from gesture import Gesture

class Player:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        self.gesture_object = Gesture()
        self.select_gesture = None

    def choose_gesture(self):
        """
        Purpose: Chooses gesture by way of polymorphism
        """
        pass
   
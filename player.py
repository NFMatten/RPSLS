from gesture import Gesture

class Player:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        self.chosen_gesture = ''
        self.gesture_object = Gesture(self.chosen_gesture)

    def choose_gesture(self):
        """
        Purpose: Chooses gesture by way of polymorphism
        """
        pass
        
        
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        self.chosen_gesture = self.choose_gesture()

    def player_scoring(self):
        """
        Purpose: If player wins round, +1 to their score
        """

    def player_gesture_selection(self):
        """
        Purpose: Player chooses gesture
        """

    def choose_gesture(self):
        pass
        
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"]

    def player_scoring(self):
        """
        Purpose: If player wins round, +1 to their score
        """

    def player_gesture_selection(self):
        """
        Purpose: Player chooses gesture
        """
        
    def is_player_two_ai(self):
        user_input = input("Is player 2 a computer or player? ")
        if user_input == "computer":
            pass
            #then create computer player object
        elif user_input == "player":
            pass
            #then create player object
        else:
            pass
            #invalid input
from player import Player

class Scoreboard:
    def __init__(self):
        player_one = Player("Name")
        player_two = Player("Name2")

    def clear_scoreboard(self):
        """
        Purpose: Clear scoreboard after game is over
        """
        self.player_one_score = 0
        self.player_two_score = 0

    def add_to_score(self, winner):
        """
        Purpose: Add score to scoreboard
        """
        winner.score += 1

from computer import Computer
from human_player import Human
class Game:
    def __init__(self):
        """
        Purpose: Initialize player 1 and player 2 objects
        """
        self.player_two = self.select_player_type()
        self.player_one = Human("Player 1")
    def select_player_type(self):
        """
        Purpose: Choose player two player type (AI or Human)
        """
        user_input = input('What is player two? Computer or Human? ')
        possible_players = ['human', 'computer']
        final_user_input = user_input.lower()
        if final_user_input not in possible_players:
            print('Invalid input, please type again. ')
            self.select_player_type()
        if final_user_input == 'human':
            return Human("Player 2")
        else:
            return Computer("Player 2 AI")
    def add_to_score(self, winner):
        """
        Purpose: Add score to scoreboard
        """
        winner.score += 1
        self.print_score()
    def print_score(self):
        """
        Purpose: Prints scoreboard
        """
        print(f'Player 1 Score: {self.player_one.score}\nPlayer 2 Score: {self.player_two.score}')
    def find_winner(self):
        """
        Purpose: Compares player 1 gesture to player 2 gestuer, determine winner
        """
        if self.player_two.selected_gesture.name in self.player_one.selected_gesture.gesture_beats:
            print("Player one wins")
            self.add_to_score(self.player_one)
        elif self.player_one.selected_gesture.name in self.player_two.selected_gesture.gesture_beats:
            print("Player two wins")
            self.add_to_score(self.player_two)
        else:
            print('It was a Tie!')
    def print_game_winner(self):
        """
        Purpose: Win a player reaches 2 points, (best 2/3), prints winner of game
        """
        if self.player_one.score == 2:
                print("Player One wins the game!")
        elif self.player_two.score == 2:
            print("Player Two wins the game!")
    def run_game(self):
        """
        Purpose: Run game for "best two out of three".
        """
        player_scores = [self.player_one.score, self.player_two.score]
        while max(player_scores) != 2:
            self.player_two.selected_gesture = self.player_two.choose_gesture() 
            self.player_one.selected_gesture = self.player_one.choose_gesture() 
            self.find_winner()
            player_scores = [self.player_one.score, self.player_two.score]
            self.print_game_winner()
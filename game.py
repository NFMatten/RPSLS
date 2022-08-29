from computer import Computer
from player import Player
from human_player import Human


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = self.select_player_type()

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

    def select_player_type(self):
        user_input = input('What is player two? Computer or Human? ')
        possible_players = ['human', 'computer']
        user_input.lower()
        if user_input in possible_players:
            print('Valid Input')
        else:
            print('Invalid input, please type again. ')
            self.select_player_type()

        if user_input == 'human':
            return Human()
        else:
            return Computer()
           

    def find_winner(self):
        player_one_gesture = self.player_one.chosen_gesture
        player_two_gesture = self.player_two.chosen_gesture

        if player_one_gesture == player_two_gesture:
            print('Invalid input')

        if player_one_gesture == 'rock':
            if player_two_gesture == 'scissors' or player_two_gesture == 'lizard':
                print('')
        if player_one_gesture == 'paper':
            pass
        if player_one_gesture == 'scissors':
            pass
        if player_one_gesture == 'lizard':
            pass
        if player_one_gesture == 'spock':
            pass
            
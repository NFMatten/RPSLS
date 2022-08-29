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
        if user_input not in possible_players:
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
            print('It was a Tie!')

        if player_one_gesture == 'rock':
            if player_two_gesture == 'scissors' or player_two_gesture == 'lizard':
                print(f'Player One Wins!')
                self.add_to_score(self.player_one.score)
            else:
                print(f'Player Two Wins!')
                self.add_to_score(self.player_two.score)
        
        if player_one_gesture == 'paper':
            if player_two_gesture == 'rock' or player_two_gesture == 'spock':
                print(f'Player One Wins!')
                self.add_to_score(self.player_one.score)
            else:
                print(f'Player Two Wins!')
                self.add_to_score(self.player_two.score)

        if player_one_gesture == 'scissors':
            if player_two_gesture == 'paper' or player_two_gesture == 'lizard':
                print(f'Player One Wins!')
                self.add_to_score(self.player_one.score)
            else:
                print(f'Player Two Wins!')
                self.add_to_score(self.player_two.score)

        if player_one_gesture == 'lizard':
            if player_two_gesture == 'paper' or player_two_gesture == 'spock':
                print(f'Player One Wins!')
                self.add_to_score(self.player_one.score)
            else:
                print(f'Player Two Wins!')
                self.add_to_score(self.player_two.score)

        if player_one_gesture == 'spock':
            if player_two_gesture == 'scissors' or player_two_gesture == 'rock':
                print(f'Player One Wins!')
                self.add_to_score(self.player_one.score)
            else:
                print(f'Player Two Wins!')
                self.add_to_score(self.player_two.score)
            
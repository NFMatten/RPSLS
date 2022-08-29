from traceback import print_stack
from computer import Computer
from player import Player
from human_player import Human


class Game:
    def __init__(self):
        self.player_two = self.select_player_type()
        self.player_one = Human("Player 1")


    def select_player_type(self):
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
        print(f'Player 1 Score: {self.player_one.score}\nPlayer 2 Score: {self.player_two.score}') 

    def find_winner(self):
        player_one_gesture = self.player_one.chosen_gesture
        player_two_gesture = self.player_two.chosen_gesture

        if player_one_gesture == player_two_gesture:
            print('It was a Tie!')

        elif player_one_gesture == 'rock':
            if player_two_gesture == 'scissors' or player_two_gesture == 'lizard':
                print(f'Player One Wins!')
                self.add_to_score(self.player_one)
            else:
                print(f'Player Two Wins!')
                self.add_to_score(self.player_two)
        
        elif player_one_gesture == 'paper':
            if player_two_gesture == 'rock' or player_two_gesture == 'spock':
                print(f'Player One Wins!')
                self.add_to_score(self.player_one)
            else:
                print(f'Player Two Wins!')
                self.add_to_score(self.player_two)

        elif player_one_gesture == 'scissors':
            if player_two_gesture == 'paper' or player_two_gesture == 'lizard':
                print(f'Player One Wins!')
                self.add_to_score(self.player_one)
            else:
                print(f'Player Two Wins!')
                self.add_to_score(self.player_two)

        elif player_one_gesture == 'lizard':
            if player_two_gesture == 'paper' or player_two_gesture == 'spock':
                print(f'Player One Wins!')
                self.add_to_score(self.player_one)
            else:
                print(f'Player Two Wins!')
                self.add_to_score(self.player_two)

        elif player_one_gesture == 'spock':
            if player_two_gesture == 'scissors' or player_two_gesture == 'rock':
                print(f'Player One Wins!')
                self.add_to_score(self.player_one)
            else:
                print(f'Player Two Wins!')
                self.add_to_score(self.player_two)
            
    def run_game(self):
        player_scores = [self.player_one.score, self.player_two.score]
        while max(player_scores) != 2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            self.find_winner()
            player_scores = [self.player_one.score, self.player_two.score]
            if self.player_one.score == 2:
                print("Player One wins!")
            elif self.player_two.score == 2:
                print("Player Two wins!")
            
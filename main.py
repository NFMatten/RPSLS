#
# Start brainstorming classes needed, how inheritance would fit into the picture, and getting setup for the project
#

classes: game_board (battlefield #from robot vs dinosaur )
        player (includes: self.player score = def player_score(), )
        computer opponent(player) # computer inherits from player class


list : gestures
scoreboard


class game_board:
    def __init__(self):
        player_one = Player("Name", player)
        player_two = Player("Name", computer)
    
    def display_welcome(self):
        print("Welcome")

    def battle_phase(self):
        pass

    def scoreboard(self):
        pass

    def display_winner(self):
        pass



user_input = int(input("(1) Rock, (2) Paper, (3) Scissors"))

if user_input == 1:
    pass
else:
    print("Invalid selection")
from random import choice

class Gesture():
    def __init__(self):
        self.name = ''
        self.gestures = ["rock", "paper", "scissors", "lizard", "spock"]
        self.chosen_gesture = ''
        self.gesture_beats = ''
    
    def print_gestures(self):
        print(f'List of Gestures: {self.gestures}')
    
    def changing_getsure(self, player, gesture):
        player.chosen_gesture = gesture

    def random_choice(self):
        comp_choice = choice(self.gestures)
        return comp_choice

    rock = {
        "gesture_name" : "rock",
        "gesture_beats" : ['scissors', 'lizard']
    }

    list_of_gestures = [rock]

    gestures = {
        "rock" : {
            "gesture_name" : "rock",
        "gesture_beats" : ['scissors', 'lizard']
        },
        "paper" : {
            "gesture_name" : "paper",
            "gesture_beats" : ['scissors', 'lizard']
        }
    }
   
from random import choice

class Gesture():
    def __init__(self, user_choice):
        self.user_choice = self.change_gesture(user_choice)
        self.name = ''
        self.gesture_beats = []
        self.possible_gestures = {
        "rock" : {
            "gesture_name" : "rock",
            "gesture_beats" : ['scissors', 'lizard']
        },
        "paper" : {
            "gesture_name" : "paper",
            "gesture_beats" : ['rock', 'spock']
        },
        "scissors" : {
            "gesture_name" : "scissors",
            "gesture_beats" : ['paper', 'lizard']
        },
        "lizard" : {
            "gesture_name" : "lizard",
            "gesture_beats" : ['paper', 'spock']
        },
        "spock" : {
            "gesture_name" : "spock",
            "gesture_beats" : ['scissors', 'rock']
        }
    }

    def change_gesture(self, gesture):
        self.name = self.possible_gestures[gesture]["gesture_name"]
        self.gesture_beats = self.possible_gestures[gesture]["gesture_beats"]

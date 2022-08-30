from gesture import Gesture

class Spock(Gesture):
    def __init__(self):
        self.name = 'spock'
        self.gesture_beats = ['scissors', 'rock']
        super().__init__()
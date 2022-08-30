from gesture import Gesture

class Spock(Gesture):
    def __init__(self):
        super().__init__()
        self.name = 'spock'
        self.gesture_beats = ['scissors', 'rock']
from gesture import Gesture

class Lizard(Gesture):
    def __init__(self):
        self.name = 'lizard'
        self.gesture_beats = ['paper', 'spock']
        super().__init__()
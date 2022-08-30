from gesture import Gesture

class Scissors(Gesture):
    def __init__(self):
        self.name = 'scissors'
        self.gesture_beats = ['paper', 'lizard']
        super().__init__()
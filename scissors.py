from gesture import Gesture

class Scissors(Gesture):
    def __init__(self):
        super().__init__()
        self.name = 'scissors'
        self.gesture_beats = ['paper', 'lizard']
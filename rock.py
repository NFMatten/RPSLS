from gesture import Gesture

class Rock(Gesture):
    def __init__(self):
        self.name = 'rock'
        self.gesture_beats = ['scissors', 'lizard']
        super().__init__()
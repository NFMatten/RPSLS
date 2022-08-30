from gesture import Gesture

class Paper(Gesture):
    def __init__(self):
        self.name = 'paper'
        self.gesture_beats = ['rock', 'spock']
        super().__init__()
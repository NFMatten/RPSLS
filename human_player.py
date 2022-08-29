from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def choose_gesture(self):
        print(f"\n{self.name}, select your gesture: ")
        for item in self.gestures:
            print(f'{item}')
        user_input = input('Select a gesture! ')
        user_input.lower()
        if user_input not in self.gestures:
            print('Invalid input, please type again.')
            self.choose_gesture()
            
        self.chosen_gesture = user_input
        
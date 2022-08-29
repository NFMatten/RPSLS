from player import Player

class Human(Player):
    def __init__(self):
        super().__init__('rick')

    def choose_gesture(self):
    
        for item in self.gestures:
            print(f'{item}')
        user_input = input('Select a gesture! ')
        user_input.lower()
        if user_input in self.gestures:
            print('Valid Input')
        else:
            print('Invalid input, please type again.')
            self.choose_gesture()

        return user_input
        
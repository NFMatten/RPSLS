from player import Player

class Human(Player):
    def __init__(self):
        super().__init__('rick')

    def choose_gesture(self):
  #      print(f"{self.}, select your gesture: ")
        for item in self.gestures:
            print(f'{item}')
        user_input = input('Select a gesture! ')
        user_input.lower()
        if user_input not in self.gestures:
            print('Invalid input, please type again.')
            self.choose_gesture()
            
        self.chosen_gesture = user_input
        
from player import Player

class Human(Player):
    def __init__(self, name):
        """
        Purpose: Constructs player object thru inheritance from Player class
        Parameter: 
            name: string
        """
        super().__init__()
        self.name = name

    def choose_gesture(self):
        """
        Purpose: Allows (human) player to choose gesture
        """
        print(f"\n{self.name}, select your gesture: ")
        for item in self.gesture_names:
            print(f'{item}')
        user_input = input('Select a gesture! ')
        final_user_input = user_input.lower()

        for item in self.gestures:
            gesture_names = []
            gesture_names.append(item.name)
            if final_user_input not in gesture_names:
                print('Invalid input, please type again.')
                final_user_input = self.choose_gesture()
            elif item.name == final_user_input:
                return item 
            else:
                print('User input was not equal to a gesture!')
        
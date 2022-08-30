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
        for item in self.gestures:
            print(f'{item}')
        user_input = input('Select a gesture! ')
        final_user_input = user_input.lower()
        if final_user_input not in self.gestures:
            print('Invalid input, please type again.')
            final_user_input = self.choose_gesture()
            
        return final_user_input
        
import random
import sefira_counter


class Game:
    num = 0
    message = "Empty"
    day = "Empty"
    won = False

    def __init__(self):
        self.game_starter()

    def number_picker(self):
        self.num = random.randint(1, 49)
        print(self.num)
        self.day = sefira_counter.input_validator(self.num)     
        return self.day
        
        



        


    def guess_num(self, guess):
        try:
            guess = int(guess)
            if guess == self.num:
                self.message = "Well Done!"
                self.won = True
                return self.game_starter()
            else:
                self.message = "Try Again"
                self.won= False
                return self.game_starter()
        except:
            return 'Please enter a number'


    def game_starter(self):
        if  self.won or self.num == 0:
            return self.number_picker()
        else:
            pass









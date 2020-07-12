import random
from sefira_counter_game import sefira_counter
import time
import multiprocessing
import threading

class Game:
    num = 0
    message = "Please enter number above"
    day = "Empty"
    won = False
    score = 0
    time_count = 20
    
    
    def __init__(self):
        #self.timer_thread = multiprocessing.Process(target=self.timer)
        #self.number_thread = multiprocessing.Process(target=self.number_picker)
        self.game_starter()
        #while self.time_count == 0:
            #self.game_starter()


    def number_picker(self):
        self.num = random.randint(1, 49)
        print(self.num)
        self.day = sefira_counter.input_validator(self.num)     
        return self.day
        
        
    # def timer(self):
    #     while self.time_count != 0:
    #         for t in range(20):
    #             time.sleep(1)
    #             self.time_count -= 1
    #             print(self.time_count)
    #     else:
    #         print('Out of time!!')
            
       


    def guess_num(self, guess):
        try:
            guess = int(guess)
            if guess == self.num:
                self.message = "Well Done!"
                self.won = True
                self.score += 1
                self.time_count = 20
                #self.timer_thread.terminate()
                self.game_starter()
            elif guess is None:
                pass
            else:
                self.message = "Try Again"
                self.won= False
                self.score -= 1
                self.game_starter()
        except:
            return 'Please enter a number'

    

    def game_starter(self):
            if self.num == 0:
                self.number_picker()
            elif  self.won:
                #while self.time_count != 0:
                 self.number_picker()  
                #self.number_thread.start()#,self.number_thread.start(), 
                    
            else:
                pass
    
    def timed_out(self):
        self.score -= 1
        self.message = "Timed Out\n Next...."
        self.number_picker()
            

    def reset(self):
        num = 0
        message = "Please enter number above"
        day = "Empty"
        won = False
        score = 0
        time_count = 20




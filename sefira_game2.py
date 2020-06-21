import random
import sefira_counter

today = {
    "number": None,
    "day": "",
    "message": "",
    "won": False

}



def number_picker():
    num = whats_num()
    today["number"] = num
    day = sefira_counter.input_validator(num)
    today["day"] = day
    print(num)



def whats_num():
    num = random.randint(1, 49)
    return num


def guess_num(guess):
    try:
        guess = int(guess)
        if guess == today["number"]:
            today["message"] = "Well Done!"
            today['won'] = True
            return game_starter()
        else:
            today["message"] = "Try Again"
            today['won']= False
            return game_starter()
    except:
        return 'Please enter a number'


def game_starter():
    if today["won"]:
        return number_picker()
    else:
        pass









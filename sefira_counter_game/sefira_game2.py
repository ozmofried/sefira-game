import random
from sefira_counter_game import sefira_counter


def number_picker():
    num = random.randint(1, 49)
    day = sefira_counter.input_validator(num)     
    return num, day
 






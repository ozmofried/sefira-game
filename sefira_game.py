import random
import sefira_counter1


def number_picker():
    num = random.randint(1, 49)
#    print(num)
    return sefira_counter1.input_validator(num), guess_num(num)

def guess_num(num):
    answered = False
    while answered == False:
        guess = int(input("Which day in Sefira does this refer to:"))
        if guess == num:
            answered = True
            print("Well Done!")
            number_picker()
        else:
            answered = False

            print("Try again")

number_picker()





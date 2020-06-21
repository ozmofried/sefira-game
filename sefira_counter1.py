the_count = {1:"Chesed",
             2:"Gevurah",
             3:"Tiferes",
             4:"Netzach",
             5:"Hod",
             6:"Yisod",
             7:"Malchus",
             8:"Malchus",
             0:"Malchus"}



def input_validator(n):
   # n = input("Please enter today's Sefirah Count:")
    n = int(n)
    if n <= 7:
        return first_week(n)
    elif n >= 8 and n <= 49 and (n % 7) != 0:
        return next_six_weeks(n)
    elif n >= 8 and n <= 49 and (n % 7) == 0:
        return malchus(n)
    else:
        print("Incorrect Input!! You don't know how to count Sefirah!!")

def first_week(n):
    for x in the_count:
        if x == n:
            print(the_count[x],"sheb' Chesed")
        else:
            False

def malchus(n):
    malchut = int(n/7)
    for x in the_count:
        if x == malchut:

            print("Malchus sheb'", the_count[x])



def next_six_weeks(n):


    the_week = int((n/7)+1)
    for x in the_count:
        if x == the_week:
            week = the_count[x]
    the_day = int(n % 7)
    for x in the_count:
        if x == the_day:
            day = the_count[x]
    print(day, " sheb'", week)


#while True:
 #   input_validator()
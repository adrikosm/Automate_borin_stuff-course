import random


def one():
    return "It is certain"


def two():
    return "It is decidedly so"


def three():
    return "Yes"


def four():
    return "Reply hazy try again"


def five():
    return "Ask again"


def six():
    return "Lol no"


def seven():
    return "Outlook not so good"


def eight():
    return "Very doubtful"


def nine():
    return "i dont know ask again"


def number_to_answer(argument):
    if argument == 1:
        return one()
    elif argument == 2:
        return two()
    elif argument == 3:
        return three()
    elif argument == 4:
        return four()
    elif argument == 5:
        return five()
    elif argument == 6:
        return six()
    elif argument == 7:
        return seven()
    elif argument == 8:
        return eight()
    else:
        return nine()


def get_int():
    while True:
        try:
            integer = int(input("Give a number "))
            return integer
        except ValueError:
            print("Give a valid number ")
            pass


print("ask a yes/no question and enter to see answer")
input()

repetition = 1
while repetition != 0:
    print(number_to_answer(random.randint(1, 9)))
    print("\n Select 0 to exit or any number to ask again")
    repetition = get_int()

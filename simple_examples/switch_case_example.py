def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y
    }.get(operator, lambda: None)()


def get_int():
    while True:
        try:
            integer = int(input("Give a number "))
            return integer
        except ValueError:
            print("Give a valid number ")
            pass


def calculate_user_choice(operator):
    return {
        1: "add",
        2: "sub",
        3: "mul",
        4: "div"
    }.get(operator, None)


print("---MENU---")
print("1:to add")
print("2:to sub")
print("3:to mul")
print("4:to div")
print("5:to exit")

user_choice = get_int()

while user_choice < 1 or user_choice > 5:
    print("Give again")
    user_choice = get_int()

if user_choice == 5:
    print("Goodbye")
    exit()

print("Give first number to operate ")
user_number_1 = get_int()
print("Give second number to operate ")
user_number_2 = get_int()

print(dispatch_dict(calculate_user_choice(user_choice)
                    , user_number_1,
                    user_number_2))

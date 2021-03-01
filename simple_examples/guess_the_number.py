import random


def get_int():
    while True:
        try:
            print("Take a guess")
            integer = int(input())
            while integer > 20 or integer < 1:
                print("Give a number between 1 and 20 plz")
                print("Take a guess")
                integer = int(input())
            return integer
        except ValueError:
            print("Give a valid number")
            pass


print("Hello , what is your name?")
user_name = input()

print(f'Well {user_name} i am thinking of a number between 1 and 20')
secret_number = random.randint(1, 20)

print(f'DEBUG:The secret number is {secret_number}')

for guesses_taken in range(1, 7):
    user_guess = get_int()
    if user_guess < secret_number:
        print(f'Guess is to low try again')
    elif user_guess > secret_number:
        print(f'Guess to high try again')
    else:
        break

if user_guess == secret_number:
    print(f'Good job {user_name} you found the secret number in {guesses_taken} guesses')
else:
    print(f'The number i was thinking of was '
          f'{secret_number} and you did not find it')

print(f'You took {guesses_taken} guesses')

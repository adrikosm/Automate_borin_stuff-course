def print_board(board):
    print(board['top-l'] + ' |' + board['top-m'] + ' |' + board['top-r'])
    print('-------')
    print(board['mid-l'] + ' |' + board['mid-m'] + ' |' + board['mid-r'])
    print('-------')
    print(board['low-l'] + ' |' + board['low-m'] + ' |' + board['low-r'])


def check_user_choice(board, choice):
    while choice not in board.keys():
        choice = input('Give choice again ')
    return choice


def check_for_horizontal_win(board):
    if board['top-l'] == board['top-m'] == board['top-r'] == 'x':
        print("Horizontal win on first line by X")
        return False
    elif board['top-l'] == board['top-m'] == board['top-r'] == 'o':
        print("Horizontal win on first line by O")
        return False
    elif board['mid-l'] == board['mid-m'] == board['mid-r'] == 'o':
        print("Horizontal win on second line by O")
        return False
    elif board['mid-l'] == board['mid-m'] == board['mid-r'] == 'x':
        print("Horizontal win on second line by x")
        return False
    elif board['low-l'] == board['low-m'] == board['low-r'] == 'o':
        print("Horizontal win on last line by O")
        return False
    elif board['low-l'] == board['low-m'] == board['low-r'] == 'x':
        print("Horizontal win on last line by x")
        return False


the_board = {
    'top-l': ' ',
    'top-m': ' ',
    'top-r': ' ',
    'mid-l': ' ',
    'mid-m': ' ',
    'mid-r': ' ',
    'low-l': ' ',
    'low-m': ' ',
    'low-r': ' '

}

print('\n')
print("Select between O and X ")
user_avatar = input()

while user_avatar != 'x' and user_avatar != 'o':
    print("Select between O and X ")
    user_avatar = input()

game_running = True
check_win = True

while game_running:
    user_choice = input("Select board space ")
    user_choice = check_user_choice(the_board, user_choice)

    the_board[user_choice] = user_avatar

    check_win = check_for_horizontal_win(the_board)

    if  check_win == False:
        print(f'{user_avatar} you won')
        break

    print_board(the_board)

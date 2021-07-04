state = ["_"] * 9
index = {
    '1 1': 0,
    '1 2': 1,
    '1 3': 2,
    '2 1': 3,
    '2 2': 4,
    '2 3': 5,
    '3 1': 6,
    '3 2': 7,
    '3 3': 8
}
finish = False
x_o = 0


def print_state():
    print("---------")
    print("|", state[0].replace("_", " "), state[1].replace("_", " "), state[2].replace("_", " "), "|")
    print("|", state[3].replace("_", " "), state[4].replace("_", " "), state[5].replace("_", " "), "|")
    print("|", state[6].replace("_", " "), state[7].replace("_", " "), state[8].replace("_", " "), "|")
    print("---------")


def x_move():
    global x_o
    while True:
        x_cord = input('Enter the coordinates: ')
        if input_ok(x_cord):
            break
    if x_o == 0:
        state[index[x_cord]] = 'X'
        x_o += 1
    else:
        state[index[x_cord]] = 'O'
        x_o -= 1
    game_state_check()


def input_ok(user_input):
    global state
    global index
    if user_input in index:
        if state[index[user_input]] == '_':
            return True
        else:
            print('This cell is occupied! Choose another one!')
            return False
    else:
        if not user_input.replace(' ', '').isdigit():
            print('You should enter numbers!')
        else:
            print('Coordinates should be from 1 to 3!')
        return False


def game_state_check():
    x_win = False
    o_win = False
    global finish
    if state[0] == state[1] == state[2]:
        if state[0] == 'X':
            x_win = True
        elif state[0] == 'O':
            o_win = True
    if state[3] == state[4] == state[5]:
        if state[3] == 'X':
            x_win = True
        elif state[3] == 'O':
            o_win = True
    if state[6] == state[7] == state[8]:
        if state[6] == 'X':
            x_win = True
        elif state[6] == 'O':
            o_win = True
    if state[0] == state[3] == state[6]:
        if state[0] == 'X':
            x_win = True
        elif state[0] == 'O':
            o_win = True
    if state[1] == state[4] == state[7]:
        if state[1] == 'X':
            x_win = True
        elif state[1] == 'O':
            o_win = True
    if state[2] == state[5] == state[8]:
        if state[2] == 'X':
            x_win = True
        elif state[2] == 'O':
            o_win = True
    if state[6] == state[4] == state[2]:
        if state[2] == 'X':
            x_win = True
        elif state[2] == 'O':
            o_win = True
    if state[0] == state[4] == state[8]:
        if state[0] == 'X':
            x_win = True
        elif state[0] == 'O':
            o_win = True
    if x_win:
        print_state()
        print('X wins')
        finish = True
    elif o_win:
        print_state()
        print('O wins')
        finish = True
    elif '_' not in state:
        print_state()
        print('Draw')
        finish = True
    else:
        pass


print_state()
while True:
    x_move()
    if finish:
        break
    print_state()

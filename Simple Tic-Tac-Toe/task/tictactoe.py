# write your code here
x_match = 0
o_match = 0


def user_input():
    coordinate_x, coordinate_y = input("Enter the coordinates:").split(" ")
    try:
        coordinate_x = int(coordinate_x)
        coordinate_y = int(coordinate_y)
    except ValueError:
        print("You should enter numbers!")
        user_input()

    if int(coordinate_x) > 3 or int(coordinate_y) > 3:
        print("Coordinates should be from 1 to 3!")
        user_input()
    place_user_input_on_location(coordinate_x, coordinate_y)


def place_user_input_on_location(x, y):
    global selection

    if x == 1 and y == 1:
        if selection[0] == "X" or selection[0] == "O":
            print("This cell is occupied! Choose another one!")
            user_input()
        else:
            selection[0] = "X"
    elif x == 1 and y == 2:
        if selection[1] == "X" or selection[1] == "0":
            print("This cell is occupied! Choose another one!")
            user_input()
        else:
            selection[1] = "X"
    elif x == 1 and y == 3:
        if selection[2] == "X" or selection[2] == "O":
            print("This cell is occupied! Choose another one!")
            user_input()
        else:
            selection[2] = "X"
    elif x == 2 and y == 1:
        if selection[3] == "X" or selection[3] == "O":
            print("This cell is occupied! Choose another one!")
            user_input()
        else:
            selection[3] = "X"
    elif x == 2 and y == 2:
        if selection[4] == "X" or selection[4] == "O":
            print("This cell is occupied! Choose another one!")
            user_input()
        else:
            selection[4] = "X"
    elif x == 2 and y == 3:
        if selection[5] == "X" or selection[5] == "O":
            print("This cell is occupied! Choose another one!")
            user_input()
        else:
            selection[5] = "X"
    elif x == 3 and y == 1:
        if selection[6] == "X" or selection[6] == "O":
            print("This cell is occupied! Choose another one!")
            user_input()
        else:
            selection[6] = "X"
    elif x == 3 and y == 2:
        if selection[7] == "X" or selection[7] == "O":
            print("This cell is occupied! Choose another one!")
            user_input()
        else:
            selection[7] = "X"
    elif x == 3 and y == 3:
        if selection[8] == "X" or selection[8] == "O":
            print("This cell is occupied! Choose another one!")
            user_input()
        else:
            selection[8] = "X"


def print_game_layout():
    global selection
    print("---------")
    print("|" + " " + selection[0] + " " + selection[1] + " " + selection[2] + " |")
    print("|" + " " + selection[3] + " " + selection[4] + " " + selection[5] + " |")
    print("|" + " " + selection[6] + " " + selection[7] + " " + selection[8] + " |")
    print("---------")


def check_for_winner():
    global selection
    global x_match
    global o_match
    if 'XXX' == selection[0] + selection[1] + selection[2] or 'XXX' == selection[3] + selection[4] + selection[5] or 'XXX' == selection[6] + selection[7] + selection[8] or 'XXX' == selection[0] + selection[3] + selection[6] or 'XXX' == selection[1] + selection[4] + selection[7] or 'XXX' == selection[2] + selection[5] + selection[8] or 'XXX' == selection[0] + selection[4] + selection[8] or 'XXX' == selection[2] + selection[4] + selection[6]:
        x_match += 1
    if 'OOO' == selection[0] + selection[1] + selection[2] or 'OOO' == selection[3] + selection[4] + selection[5] or 'OOO' == selection[6] + selection[7] + selection[8] or 'OOO' == selection[0] + selection[3] + selection[6] or 'OOO' == selection[1] + selection[4] + selection[7] or 'OOO' == selection[2] + selection[5] + selection[8] or 'OOO' == selection[0] + selection[4] + selection[8] or 'OOO' == selection[2] + selection[4] + selection[6]:
        o_match += 1
    if x_match > 0:
        return 1  # x wins
    elif o_match > 0:
        return 0  # o wins


user_selection = "_________"
user_selection = user_selection.replace("_", " ")
selection = list()

for i in range(0, 9):
    selection.append(user_selection[i])

print_game_layout()
while True:
    user_input()
    print_game_layout()
    winner = check_for_winner()
    if winner == 1:
        print("X wins")
        break
    elif winner == 0:
        print("O wins")
        break

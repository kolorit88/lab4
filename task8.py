def tic_tak_toe(field):
    win_team = ""
    for i, row in enumerate(field):
        if row[0] == row[1] == row[2] != "-":
            win_team = row[0]

        if field[0][i] == field[1][i] == field[2][i] != "-":
            win_team = field[0][i]

    if field[0][0] == field[1][1] == field[2][2] != "-":
        win_team = field[0][0]
    elif field[0][2] == field[1][1] == field[0][0] != "-":
        win_team = field[0][2]
    if win_team == "":
        return "draw"
    return f"{win_team} win"


data = ("0 - 0\n"
        "x x x\n"
        "0 0 -")

data2 = ("0 - 0\n"
        "x 0 x\n"
        "0 x 0")

data3 = ("- - -\n"
        "x 0 x\n"
        "0 x 0")

field = [line.split() for line in data.split("\n")]
field2 = [line.split() for line in data2.split("\n")]
field3 = [line.split() for line in data3.split("\n")]
print(tic_tak_toe(field))
print(tic_tak_toe(field2))
print(tic_tak_toe(field3))
from os import system, name

#Tic Tac Toe
field = ["_" for x in range(9)]

def clear():
    print(name)
    system("cls") if name == "nt" else system("clear")

def board():
    print("-------")
    print("|"+ field[0] + "|" + field[1] + "|" + field[2] + "|")
    print("-------")
    print("|"+ field[3] + "|" + field[4] + "|" + field[5] + "|")
    print("-------")
    print("|"+ field[6] + "|" + field[7] + "|" + field[8] + "|")
    print("-------")
    """tab = 0
    for char in field:
        print(char + ' ', end = '')
        tab += 1
        if tab % 3 == 0:
            print("\n")"""

def playerO():
    plr = None
    try:
        plr = int(input("O: "))-1
    except ValueError:
        input("Není číslo")
        clear()
        board()
        playerO()

    if plr >= 0 and plr <= 8:
        if field[plr] == "_":
            field[plr] = "O"
        else:
            input("Místo není prázdné")
            clear()
            board()
            playerO()
    else:
        input("Číslo musí být 1 - 9")
        clear()
        board()
        playerO()

def playerX():
    plr = None
    try:
        plr = int(input("X: "))-1
    except ValueError:
        input("Není číslo")
        clear()
        board()
        playerX()
        
    if plr >= 0 and plr <= 8:
        if field[plr] == "_":
            field[plr] = "X"
        else:
            input("Místo není prázdné")
            clear()
            board()
            playerX()
    else:
        input("Číslo musí být 1 - 9")
        clear()
        board()
        playerX()

def win():
    if "O" == field[0] == field[1] == field[2]: #rows
        clear(); board(); input("O vyhrálo"); quit()
    elif "O" == field[3] == field[4] == field[2]:
        clear(); board(); input("O vyhrálo"); quit()
    elif "O" == field[6] == field[7] == field[8]:
        clear(); board(); input("O vyhrálo"); quit()
    elif "O" == field[0] == field[3] == field[6]: #cols
        clear(); board(); input("O vyhrálo"); quit()
    elif "O" == field[1] == field[4] == field[7]:
        clear(); board(); input("O vyhrálo"); quit()
    elif "O" == field[2] == field[5] == field[8]:
        clear(); board(); input("O vyhrálo"); quit()
    elif "O" == field[0] == field[4] == field[8]: #diagonal
        clear(); board(); input("O vyhrálo"); quit()
    elif "O" == field[2] == field[4] == field[6]:
        clear(); board(); input("O vyhrálo"); quit()
    
    elif "X" == field[0] == field[1] == field[2]: #rows
        clear(); board(); input("X vyhrál"); quit()
    elif "X" == field[3] == field[4] == field[5]:
        clear(); board(); input("X vyhrál"); quit()
    elif "X" == field[6] == field[7] == field[8]:
        clear(); board(); input("X vyhrál"); quit()
    elif "X" == field[0] == field[3] == field[6]: #cols
        input("X vyhrál"); quit()
    elif "X" == field[1] == field[4] == field[7]:
        clear(); board(); input("X vyhrál"); quit()
    elif "X" == field[2] == field[5] == field[8]:
        clear(); board(); input("X vyhrál"); quit()
    elif "X" == field[0] == field[4] == field[8]: #diagonal
        clear(); board(); input("X vyhrál"); quit()
    elif "X" == field[2] == field[4] == field[6]:
        clear(); board(); input("X vyhrál"); quit()
    
    elif "_" not in field:
        clear(); board(); input("Remíza"); quit()

clear()
print("Zadejte jen hodnoty 1-9")
while True:
    board()
    playerO()
    win()
    clear()
    board()
    playerX()
    win()
    clear()

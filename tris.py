# --- GIOCO TRIS ---
turn = 'X'  # turno iniziale

theBoard = {1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '}

win_conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                 [1, 4, 7], [2, 5, 8], [3, 6, 9],
                 [1, 5, 9], [3, 5, 7]]


def printboard(board):
    print(f''' {board[1]}  |  {board[2]}  |  {board[3]}
---------------\n {board[4]}  |  {board[5]}  |  {board[6]}
---------------\n {board[7]}  |  {board[8]}  |  {board[9]}''')


def switch_turn(t):
    if t == 'X':
        return 'O'
    else:
        return 'X'


def win_check():
    for condition in win_conditions:
        if theBoard[condition[0]] == theBoard[condition[1]] ==\
           theBoard[condition[2]] and theBoard[condition[0]] != ' ':
            printboard(theBoard)
            print(f'\n{theBoard[condition[0]]} HA VINTO!')
            return True
    return False


def draw_check():
    if win_check() == False and ' ' not in theBoard.values():
        printboard(theBoard)
        print('PAREGGIO!')
        return True


while True:  # main loop
    print()
    printboard(theBoard)
    
    mossa = int(input(f'Turno di {turn}. Quale spazio vuoi? '))
    
    while mossa not in theBoard:
        mossa = int(input('Input non valido. Inserisci un numero da 1 a 9: '))
    while theBoard[mossa] != ' ':
        mossa = int(input('Casella già occupata. Scegli ancora: '))
    
    theBoard[mossa] = turn
    turn = switch_turn(turn)
    if win_check() or draw_check():
        break